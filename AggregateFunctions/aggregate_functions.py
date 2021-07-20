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

    def sum_function(self):
        """
        Description:
            This function will give the sum of entries in particular column.
        """
        try:
            my_cursor = db_connection.cursor()
            sum_query = "select sum(salary) as 'total_salary' from employee_details"
            my_cursor.execute(sum_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def avg_function(self):
        """
        Description:
            This function will give the average of entries in particular column.
        """
        try:
            my_cursor = db_connection.cursor()
            avg_query = "select avg(salary) as 'average salary' from employee_details"
            my_cursor.execute(avg_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def min_function(self):
        """
        Description:
            This function will give the minimum value in particular column.
        """
        try:
            my_cursor = db_connection.cursor()
            min_query = "select min(salary) as 'minimum salary' from employee_details"
            my_cursor.execute(min_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def max_function(self):
        """
        Description:
            This function will give the maximum value in particular column.
        """
        try:
            my_cursor = db_connection.cursor()
            max_query = "select max(salary) as 'minimum salary' from employee_details"
            my_cursor.execute(max_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def first_function(self):
        """
        Description:
            This function will give the first value in particular column.
        """
        try:
            my_cursor = db_connection.cursor()
            first_query = "select salary from employee_details limit 1"
            my_cursor.execute(first_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def last_function(self):
        """
        Description:
            This function will give the last value in particular column.
        """
        try:
            my_cursor = db_connection.cursor()
            last_query = "select employee_name from employee_details order by employee_name desc limit 1"
            my_cursor.execute(last_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

aggregate = AggregateFunctions()
aggregate.count_function()
aggregate.sum_function()
aggregate.avg_function()
aggregate.min_function()
aggregate.max_function()
aggregate.first_function()
aggregate.last_function()
