'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-21
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-21
@Title : Program for MySQL sorted procedures
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

class SortedProcedures():

    def create_procedure(self):
        """
        Description:
            This function will create sorted procedure for given table in database.
        """
        try:
            my_cursor = db_connection.cursor()
            create_procedure_query ="create procedure emp_info() begin select * from employee_details where salary >30000; select count(name) as total_emp from employee_details; end"
            my_cursor.execute(create_procedure_query)
            logger.info("sorted procedure created")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

procedure_obj = SortedProcedures()
procedure_obj.create_procedure()

