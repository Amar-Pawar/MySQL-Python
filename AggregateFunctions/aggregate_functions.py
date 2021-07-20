'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-20
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-20
@Title : Program to perform various aggregate operations of database
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
class AggregateFunctions():

    def count_function(self):
        """
        Description:
            This function will count the entries based on query.
        """
        try:
            my_cursor = db_connection.cursor()
            count_query ="select count(employee_name) from employee_details"
            my_cursor.execute(count_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

aggregate = AggregateFunctions()
aggregate.count_function()
