from flask import Flask, request, jsonify
import logging
import time
from logging.handlers import TimedRotatingFileHandler
from logstash_async.handler import AsynchronousLogstashHandler
from logstash_async.formatter import FlaskLogstashFormatter
import psycopg2
from dotenv import load_dotenv
from datetime import datetime
from functools import wraps
import os
import re
from celery import Celery
from constants import *
from utils import *
from queries import *


# Set up logging
def init_logger_def():
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    try:
        handler = TimedRotatingFileHandler(
            "./logs/debug.log", when="midnight", interval=1)
    except:
        handler = TimedRotatingFileHandler(
            "../logs/debug.log", when="midnight", interval=1)
    handler.setLevel("DEBUG")
    formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
    handler.setFormatter(formatter)
    # add a suffix which you want
    handler.suffix = "%Y%m%d"
    # need to change the extMatch variable to match the suffix for it
    handler.extMatch = re.compile(r"^\d{8}$")
    logger.addHandler(handler)

    return logger


load_dotenv()

DATABASE_HOST = os.getenv('db_host')
DATABASE_PORT = os.getenv('db_port')
DATABASE_USER_NAME = os.getenv('db_user_name')
DATABASE_PASSWORD = os.getenv('db_password')
DATABASE_NAME = os.getenv('db_name')
DATABASE_SCHEMA = os.getenv('db_schema')
DATABASE_TABLE = os.getenv('db_table')

api = Flask(__name__)
# Celery configuration
api.config['CELERY_BROKER_URL'] = os.getenv('celery_broker_url')
api.config['CELERY_RESULT_BACKEND'] = os.getenv('celery_result_backend')

max_retries = os.getenv('max_retries')
retry_backoff = os.getenv('retry_backoff')
logstash_host = os.getenv('logstash_host')
logstash_port = os.getenv('logstash_port')

# Initialize Celery
RESULT_EXPIRE_TIME = 60 * 60 * 4
celery = Celery(api.name, broker=api.config['CELERY_BROKER_URL'], result_backend=api.config['CELERY_RESULT_BACKEND'], result_expires=RESULT_EXPIRE_TIME)
celery.conf.update(api.config)


# Initialize Logstash
def init_logstash_logger():
    logstash_handler = AsynchronousLogstashHandler(
        logstash_host,
        int(logstash_port),
        database_path=None,
        transport='logstash_async.transport.BeatsTransport'
    )
    logstash_handler.formatter = FlaskLogstashFormatter(metadata={"beat": "mpc-odk"})
    logger = logging.getLogger("#logstash_logger")
    logger.addHandler(logstash_handler)
    return logger


#logstash_logger = init_#logstash_logger()
logger = init_logger_def()


def timed(func):
    """This decorator prints the execution time for the decorated function."""

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        try:
            instanceID = request.get_json()['data'][0][0]['instanceID']
            result = func(*args, **kwargs)
            end = time.time()
            logger.info("ODK-LOGS: {} ran in {}s: instanceID=>{}".format(func.__name__, round(end - start, 2), instanceID.replace("uuid:", "")))
            #logstash_logger.info("ODK-LOGS: {} ran in {}s: instanceID=>{}".format(func.__name__, round(end - start, 2), instanceID.replace("uuid:", "")))
        except Exception as error:
            logger.error("ODK-LOGS: Exception in {} - {} : {}".format(func.__name__, type(error).__name__, error))
            #logstash_logger.error("ODK-LOGS: Exception in {} - {} : {}".format(func.__name__, type(error).__name__, error))
            return "error", 404
        return result

    return wrapper


def get_connection():
    """ Connect to the database server
    Args:
        conn_string: database connection string
    Returns:
        connection object
    """
    conn = None
    try:
        # logger.info('Connecting to the database ...')
        conn = psycopg2.connect(
            user=DATABASE_USER_NAME,
            password=DATABASE_PASSWORD,
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            database=DATABASE_NAME)
    except Exception as e:
        logger.error(e)
    return conn


@api.route('/')
def starting_url():
    data = {'status': 'OK'}
    #logstash_logger.info(data)
    return jsonify(data)


@celery.task(max_retries=max_retries, retry_backoff=retry_backoff, autoretry_for=(Exception, psycopg2.Error))
def add_task(data, query, param_list):
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # Store data in main dump table
        cursor.execute(query, get_tuple_from_dict(data, param_list))
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        logger.error(f"Error in update operation {error}")
        #logstash_logger.error(f"Error in update operation {error}")
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            # logger.info("PostgreSQL connection is closed")


@api.route('/volunteer', methods=['POST'])
@timed
def save_volunteer():
    request_json = request.json
    if not request_json["formId"]:
        logger.error(f'No formId in the input payload')
        return "error", 404
    if not request_json["data"]:
        logger.error(f'No data in the input payload')
        return "error", 404
    else:
        for form_response in request_json["data"]:
            form_response = form_response[0]
            if not form_response['today']:
                form_response['today'] = str((datetime.now()).date())
            form_response['instanceID'] = form_response['instanceID'].replace("uuid:", "")
            add_task.delay(form_response, INSERT_VOLUNTEER, VOLUNTEER_DICT_PARAMS)
            add_task.delay(form_response, INSERT_VOLUNTEER_NORMALISED, VOLUNTEER_NORMALISED_DICT_PARAMS)
    # logger.info(f"Received request successfully")
    return "success"


@api.route('/epathshala-quiz', methods=['POST'])
@timed
def save_e_pathshala_quiz_data():
    request_json = request.json
    #logger.info(f'Quiz form Input JSON is:  {request_json}')

    if not request_json["formId"]:
        logger.info(f'No formId in the input payload')
        return "error", 404
    if not request_json["data"]:
        logger.error(f'No data in the input payload')
        return "error", 404
    else:
        for form_response in request_json["data"]:
            form_response = form_response[0]
            if not form_response['today']:
                form_response['today'] = str((datetime.now()).date())
            form_response['instanceID'] = form_response['instanceID'].replace("uuid:", "")
            normalised_dict = build_dict_epathshala(form_response)
            add_task.delay(normalised_dict, INSERT_EPATHSHALA, EPATHSHALA_DICT_PARAMS)
    # logger.info(f"Quiz form Submission received request successfully")
    return "success"


if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8080)
