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

    def create_view():
        """
        Description:
            This function will create mysql view from given columns from table.
        """
        try:
            my_cursor = db_connection.cursor()
            create_view_query ="create view emp_info as select name,salary from employee_details"
            my_cursor.execute(create_view_query)
        except Exception as e:
            print(f"Errorr!!{e}")

view_object = MysqlViews()
view_object.create_view()