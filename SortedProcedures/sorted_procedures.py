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

    def call_procedure(self):
        """
        Description:
            This function will call the sorted procedure created.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.callproc('emp_info')
            for result in my_cursor.stored_results():
                logger.info(result.fetchall())
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def procedure_in_param(self):
        """
        Description:
            This function will create sorted procedure with in parameter for given table in database.
        """
        try:
            my_cursor = db_connection.cursor()
            create_procedure_query ="create procedure emp_data(in var1 int) begin select * from employee_details limit var1; select count(name) as total_emp from employee_details; end"
            my_cursor.execute(create_procedure_query)
            logger.info("sorted procedure created")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def call_in_param_procedure(self):
        """
        Description:
            This function will call the sorted procedure with in parameter.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.callproc('emp_data',[2,])
            for result in my_cursor.stored_results():
                logger.info(result.fetchall())
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def procedure_out_param(self):
        """
        Description:
            This function will create sorted procedure with out parameter for given table in database.
        """
        try:
            my_cursor = db_connection.cursor()
            out_procedure_query ="create procedure max_salary(out maxsalary int) begin select max(salary) into maxsalary from employee_details; end"
            my_cursor.execute(out_procedure_query)
            logger.info("sorted procedure created")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def call_out_param_procedure(self):
        """
        Description:
            This function will call the sorted procedure with out parameter.
        """
        try:
            my_cursor = db_connection.cursor()
            result = my_cursor.callproc('max_salary', ['@M'])
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def list_procedures(self):
        """
        Description:
            This function will list all the sorted procedure.
        """
        try:
            my_cursor = db_connection.cursor()
            list_query = "show procedure status where Db = 'employee'"
            my_cursor.execute(list_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

procedure_obj = SortedProcedures()
procedure_obj.create_procedure()
procedure_obj.call_procedure()
procedure_obj.procedure_in_param()
procedure_obj.call_in_param_procedure()
procedure_obj.procedure_out_param()
procedure_obj.call_out_param_procedure()
procedure_obj.list_procedures()

