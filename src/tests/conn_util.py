import psycopg2

def get_connection():
    DATABASE_HOST = '127.0.0.1'
    DATABASE_PORT = '5432'
    DATABASE_USER_NAME ='postgres'
    DATABASE_PASSWORD = 'test@123'
    DATABASE_NAME = 'odk_data_automation'
    #DATABASE_SCHEMA = os.getenv('db_schema')
    #DATABASE_TABLE = os.getenv('db_table')

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