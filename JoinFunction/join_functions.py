'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-20
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-20
@Title : Program to perform various join operations of database tables
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
class JoinFunction():

    def inner_join(self):
        """
        Description:
            This function will create inner join between two tables and find intersecting values.
        """
        try:
            my_cursor = db_connection.cursor()
            inner_join_query ="select employee_details.id,employee_details.name,employee_details.salary,department.department_id,department.dept_name from department join employee_details on department.department_id = employee_details.department_id"
            my_cursor.execute(inner_join_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def right_join(self):
        """
        Description:
            This function will create right join between two tables.
        """
        try:
            my_cursor = db_connection.cursor()
            right_join_query ="select employee_details.id,employee_details.name,employee_details.salary,department.department_id,department.dept_name from department right join employee_details on department.department_id = employee_details.department_id"
            my_cursor.execute(right_join_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def left_join(self):
        """
        Description:
            This function will create left join between two tables.
        """
        try:
            my_cursor = db_connection.cursor()
            left_join_query ="select employee_details.id,employee_details.name,employee_details.salary,department.department_id,department.dept_name from department left join employee_details on department.department_id = employee_details.department_id"
            my_cursor.execute(left_join_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

join_object = JoinFunction()
join_object.inner_join()
join_object.right_join()
join_object.left_join()
