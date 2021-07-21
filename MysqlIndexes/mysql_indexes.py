'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-21
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-21
@Title : Program for MySQL indexes
/**********************************************************************************
'''
import sys
sys.path.insert(0, '/home/ubuntu/Documents/PythonWorkspace/MySQL-Operations')
from CrudOperations.logging_handler import logger
import mysql.connector
import os
from dotenv import load_dotenv
load_dotenv()

db_connection = mysql.connector.connect(
     host = os.environ.get("DB_HOST"),
     user = os.environ.get("DB_USER"),
     passwd= os.environ.get("DB_PASSWORD"),
     auth_plugin = os.environ.get("AUTH_PLUGIN"),
     database = os.environ.get("DATABASE")
    )

class MysqlIndexes():

    def create_index(self):
        """
        Description:
            This function will create index for particular table.
        """
        try:
            my_cursor = db_connection.cursor()
            create_index_query ="create index salary on employee_details(salary)"
            my_cursor.execute(create_index_query)
            logger.info("Index for given table created")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

index_obj = MysqlIndexes()
index_obj.create_index()
