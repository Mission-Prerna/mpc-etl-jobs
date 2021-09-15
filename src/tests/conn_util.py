import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_HOST = os.getenv('db_host')
DATABASE_PORT = os.getenv('db_port')
DATABASE_USER_NAME = os.getenv('db_user_name')
DATABASE_PASSWORD = os.getenv('db_password')
DATABASE_NAME = os.getenv('db_name')
DATABASE_SCHEMA = os.getenv('db_schema')
DATABASE_TABLE = os.getenv('db_table')
def get_connection():

    """ Connect to the database server
        Args:
            conn_string: database connection string
        Returns:
            connection object
        """
    conn = None
    try:
        #api.logger.info('Connecting to the database ...')
        conn = psycopg2.connect(
            user=DATABASE_USER_NAME,
            password=DATABASE_PASSWORD,
            host=DATABASE_HOST,
            port=DATABASE_PORT,
            database=DATABASE_NAME)
    except Exception as e:
        #api.logger.error(e)
        print("Exception")
    return conn