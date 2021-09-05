from flask import Flask, request, jsonify
import logging
from logging.handlers import TimedRotatingFileHandler
import psycopg2
from dotenv import load_dotenv
from datetime import datetime
import os
import re

# Set up logging
from psycopg2.extras import execute_values

logger = logging.getLogger()
logger.setLevel(logging.INFO)
handler = TimedRotatingFileHandler("./logs/debug.log", when="midnight", interval=1)
handler.setLevel("DEBUG")
formatter = logging.Formatter('%(asctime)s %(levelname)s:%(message)s')
handler.setFormatter(formatter)
# add a suffix which you want
handler.suffix = "%Y%m%d"
#need to change the extMatch variable to match the suffix for it
handler.extMatch = re.compile(r"^\d{8}$") 
logger.addHandler(handler)

load_dotenv()

DATABASE_HOST = os.getenv('db_host')
DATABASE_PORT = os.getenv('db_port')
DATABASE_USER_NAME = os.getenv('db_user_name')
DATABASE_PASSWORD = os.getenv('db_password')
DATABASE_NAME = os.getenv('db_name')
DATABASE_SCHEMA = os.getenv('db_schema')
DATABASE_TABLE = os.getenv('db_table')

api = Flask(__name__)

def get_connection():
    """ Connect to the database server
    Args:
        conn_string: database connection string
    Returns:
        connection object
    """
    conn = None
    try:
        api.logger.info('Connecting to the database ...')
        conn = psycopg2.connect(
            user=DATABASE_USER_NAME, 
            password=DATABASE_PASSWORD, 
            host=DATABASE_HOST, 
            port=DATABASE_PORT,
            database=DATABASE_NAME)
    except Exception as e:
        api.logger.error(e)
    return conn

@api.route('/')
def starting_url():
    data = {'status': 'OK'}
    return jsonify(data)

@api.route('/volunteer', methods=['POST'])
def save_volunteer():
    request_json = request.json
    if not request_json["formId"]:
        api.logger.error(f'No formId in the input payload')
        return "error"
    if not request_json["data"]:
        api.logger.error(f'No data in the input payload')
        return "error"
    else:
        final_responses = []
        final_response_normalised = []
        for form_response in request_json["data"]:
            if not form_response["today"]:
                form_response["today"] = str((datetime.now()).date())
            final_responses.append((form_response["wanum"],
            form_response["name"],
            form_response["gender"],
            form_response["age"],
            form_response["phnum"],
            form_response["school"],
            form_response["optstuno"],
            form_response["stuname1"],
            form_response["grade1"],
            form_response["stumno1"],
            form_response["stuname2"],
            form_response["grade2"],
            form_response["stumno2"],
            form_response["stuname3"],
            form_response["grade3"],
            form_response["stumno3"],
            form_response["stuname4"],
            form_response["grade4"],
            form_response["stumno4"],
            form_response["stuname5"],
            form_response["grade5"],
            form_response["stumno5"],
            form_response["stuname6"],
            form_response["grade6"],
            form_response["stumno6"],
            form_response["stuname7"],
            form_response["grade7"],
            form_response["stumno7"],
            form_response["stuname8"],
            form_response["grade8"],
            form_response["stumno8"],
            form_response["stuname9"],
            form_response["grade9"],
            form_response["stumno9"],
            form_response["stuname10"],
            form_response["grade10"],
            form_response["stumno10"],
            form_response["deviceid"],
            form_response["today"],
            form_response["instanceID"],
            form_response["name"],
            form_response["gender"],
            form_response["age"],
            form_response["phnum"],
            form_response["school"],
            form_response["optstuno"],
            form_response["stuname1"],
            form_response["grade1"],
            form_response["stumno1"],
            form_response["stuname2"],
            form_response["grade2"],
            form_response["stumno2"],
            form_response["stuname3"],
            form_response["grade3"],
            form_response["stumno3"],
            form_response["stuname4"],
            form_response["grade4"],
            form_response["stumno4"],
            form_response["stuname5"],
            form_response["grade5"],
            form_response["stumno5"],
            form_response["stuname6"],
            form_response["grade6"],
            form_response["stumno6"],
            form_response["stuname7"],
            form_response["grade7"],
            form_response["stumno7"],
            form_response["stuname8"],
            form_response["grade8"],
            form_response["stumno8"],
            form_response["stuname9"],
            form_response["grade9"],
            form_response["stumno9"],
            form_response["stuname10"],
            form_response["grade10"],
            form_response["stumno10"],
            form_response["deviceid"],
            form_response["today"],
            form_response["instanceID"]))

            final_response_normalised.append((form_response["school"],
            form_response["stuname1"],
            form_response["grade1"],
            form_response["stumno1"],
            form_response["school"],
            form_response["stuname2"],
            form_response["grade2"],
            form_response["stumno2"],
            form_response["school"],
            form_response["stuname3"],
            form_response["grade3"],
            form_response["stumno3"],
            form_response["school"],
            form_response["stuname4"],
            form_response["grade4"],
            form_response["stumno4"],
            form_response["school"],
            form_response["stuname5"],
            form_response["grade5"],
            form_response["stumno5"],
            form_response["school"],
            form_response["stuname6"],
            form_response["grade6"],
            form_response["stumno6"],
            form_response["school"],
            form_response["stuname7"],
            form_response["grade7"],
            form_response["stumno7"],
            form_response["school"],
            form_response["stuname8"],
            form_response["grade8"],
            form_response["stumno8"],
            form_response["school"],
            form_response["stuname9"],
            form_response["grade9"],
            form_response["stumno9"],
            form_response["school"],
            form_response["stuname10"],
            form_response["grade10"],
            form_response["stumno10"]))
    try:
        connection = get_connection()
        cursor = connection.cursor()
        # Store data in main dump table
        sql = """INSERT INTO prerna_saathi_final
            (whatsapp_number, volunteer_name, gender, age, phone_number, school_udise_code, student_opted_number, student_1_name, student_1_grade, student_1_number,student_2_name,  student_2_grade, student_2_number,student_3_name,  student_3_grade, student_3_number,  student_4_name, student_4_grade, student_4_number, student_5_name,student_5_grade, student_5_number, student_6_name, student_6_grade,  student_6_number, student_7_name, student_7_grade, student_7_number, student_8_name, student_8_grade, student_8_number, student_9_name, student_9_grade, student_9_number, student_10_name,student_10_grade, student_10_number, device_id, registration_date, instance_id  ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            ON CONFLICT (whatsapp_number)
            DO UPDATE SET volunteer_name = %s, gender = %s, age = %s, phone_number = %s, school_udise_code = %s, student_opted_number = %s, student_1_name = %s, student_1_grade = %s, student_1_number = %s,student_2_name = %s,  student_2_grade = %s, student_2_number = %s,student_3_name = %s,  student_3_grade = %s, student_3_number = %s,  student_4_name = %s, student_4_grade = %s, student_4_number = %s, student_5_name = %s,student_5_grade = %s, student_5_number = %s, student_6_name = %s, student_6_grade = %s,  student_6_number = %s, student_7_name = %s, student_7_grade = %s, student_7_number = %s, student_8_name = %s, student_8_grade = %s, student_8_number = %s, student_9_name = %s, student_9_grade = %s, student_9_number = %s, student_10_name = %s,student_10_grade = %s, student_10_number = %s, device_id = %s, registration_date = %s, instance_id = %s
            """
        execute_values(cursor, sql, final_responses)
        connection.commit()

        # Store data in Normalized table
        normalize_table_sql = """INSERT INTO prerna_saathi_final_normalized
            (school_udise_code, student_name, student_grade, student_number) VALUES (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s), (%s, %s, %s, %s)
            """
        execute_values(cursor, normalize_table_sql, final_response_normalised)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        api.logger.error(f"Error in update operation {error}")
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            api.logger.info("PostgreSQL connection is closed")

    api.logger.info(f'Input JSON is:  {request.json}')
    api.logger.info(f"Received request successfully")
    return "success"


@api.route('/epathshala-quiz', methods=['POST'])
def save_e_pathshala_quiz_data():
    request_json = request.json
    api.logger.info(f'Quiz form Input JSON is:  {request_json}')

    if not request_json["formId"]:
        api.logger.error(f'No formId in the input payload')
        return "error"
    if not request_json["data"]:
        api.logger.error(f'No data in the input payload')
        return "error"
    else:
        final_responses = []
        for form_response in request_json["data"]:
            if not form_response["today"]:
                form_response["today"] = str((datetime.now()).date())
            # Store data in main dump table
            deviceid = form_response["deviceid"]
            phoneno = form_response["phnum"]
            udise = form_response["school"]
            stuname = form_response["name"]
            grade = form_response["grade"]
            quizno = form_response["quiz_value"]
            subject = "Hindi"
            quizstatus = "C"
            if grade == "3":
                q1 = form_response["ques_3_hindi_1_ans"]
                q2 = form_response["ques_3_hindi_2_ans"]
                q3 = form_response["ques_3_hindi_3_ans"]
                q4 = form_response["ques_3_hindi_4_ans"]
                q5 = form_response["ques_3_hindi_5_ans"]
                q6 = form_response["ques_3_maths_1_ans"]
                q7 = form_response["ques_3_maths_2_ans"]
                q8 = form_response["ques_3_maths_3_ans"]
                q9 = form_response["ques_3_maths_4_ans"]
                q10 = form_response["ques_3_maths_5_ans"]
            elif grade == "4":
                q1 = form_response["ques_4_hindi_1_ans"]
                q2 = form_response["ques_4_hindi_2_ans"]
                q3 = form_response["ques_4_hindi_3_ans"]
                q4 = form_response["ques_4_hindi_4_ans"]
                q5 = form_response["ques_4_hindi_5_ans"]
                q6 = form_response["ques_4_maths_1_ans"]
                q7 = form_response["ques_4_maths_2_ans"]
                q8 = form_response["ques_4_maths_3_ans"]
                q9 = form_response["ques_4_maths_4_ans"]
                q10 = form_response["ques_4_maths_5_ans"]
            elif grade == "5":
                q1 = form_response["ques_5_hindi_1_ans"]
                q2 = form_response["ques_5_hindi_2_ans"]
                q3 = form_response["ques_5_hindi_3_ans"]
                q4 = form_response["ques_5_hindi_4_ans"]
                q5 = form_response["ques_5_hindi_5_ans"]
                q6 = form_response["ques_5_maths_1_ans"]
                q7 = form_response["ques_5_maths_2_ans"]
                q8 = form_response["ques_5_maths_3_ans"]
                q9 = form_response["ques_5_maths_4_ans"]
                q10 = form_response["ques_5_maths_5_ans"]
            else:
                q1 = q2 = q3 = q4 = q5 = q6 = q7 = q8 = q9 = q10 = None
            totmarks = form_response["total_score"]
            maxmarks = 10
            instance_id = form_response["instanceID"]
            final_responses.append((deviceid,
                                    phoneno,
                                    udise,
                                    stuname,
                                    grade,
                                    quizno,
                                    subject,
                                    quizstatus,
                                    q1,
                                    q2,
                                    q3,
                                    q4,
                                    q5,
                                    q6,
                                    q7,
                                    q8,
                                    q9,
                                    q10,
                                    totmarks,
                                    maxmarks,
                                    instance_id))
    try:
        connection = get_connection()
        cursor = connection.cursor()
        sql = """INSERT INTO epathshala_quiz_responses1
            (deviceid, phoneno, udise, stuname, grade, quizno, subject, quizstatus, q1, q2, q3,  q4, q5, q6,  q7, q8,  q9, q10, totmarks, maxmarks, instance_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        execute_values(cursor, sql, final_responses)
        connection.commit()
    except (Exception, psycopg2.Error) as error:
        api.logger.error(f"Error in update operation {error}")
    finally:
        # closing database connection.
        if connection:
            cursor.close()
            connection.close()
            api.logger.info("PostgreSQL connection is closed")
    api.logger.info(f"Quiz form Submission received request successfully")
    return "success"

if __name__ == '__main__':
    api.run(host='0.0.0.0', port=8080)
