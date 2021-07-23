'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-22
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-22
@Title : Program for MySQL subqueries.
/**********************************************************************************
'''
from re import sub
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

class SubQueries():

    def simple_subquery(self):
        """
        Description:
            This function will demonstrate use of simple subquery.
        """
        try:
            my_cursor = db_connection.cursor()
            sub_query ="select name, salary from employee_details where department_id in(select department_id from employee_details)"
            my_cursor.execute(sub_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def subquery_with_operator(self):
        """
        Description:
            This function will demonstrate use of subquery with comparison operator.
        """
        try:
            my_cursor = db_connection.cursor()
            sub_query ="select * from employee_details where id in (select id from employee_details where salary > 40000)"
            my_cursor.execute(sub_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

subquery_obj = SubQueries()
subquery_obj.simple_subquery()
subquery_obj.subquery_with_operator()