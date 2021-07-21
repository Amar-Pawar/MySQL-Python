'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-21
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-21
@Title : Program for MySQL views
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

class MysqlViews():

    def create_view(self):
        """
        Description:
            This function will create mysql view from given columns from table.
        """
        try:
            my_cursor = db_connection.cursor()
            create_view_query ="create view emp_info as select name,salary from employee_details"
            my_cursor.execute(create_view_query)
            logger.info("View created")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def display_view(self):
        """
        Description:
            This function will create mysql view from given columns from table.
        """
        try:
            my_cursor = db_connection.cursor()
            show_view_query = ("select * from emp_info")
            my_cursor.execute(show_view_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

view_object = MysqlViews()
view_object.create_view()
view_object.display_view()