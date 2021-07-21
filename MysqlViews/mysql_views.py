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
            This function will display view that created.
        """
        try:
            my_cursor = db_connection.cursor()
            show_view_query = ("select * from emp_info")
            my_cursor.execute(show_view_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def update_view(self):
        """
        Description:
            This function will update view.
        """
        try:
            my_cursor = db_connection.cursor()
            update_view_query = ("alter view emp_info as select id,name,salary from employee_details")
            my_cursor.execute(update_view_query)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def display_updated_view(self):
        """
        Description:
            This function will display updated view that created.
        """
        try:
            my_cursor = db_connection.cursor()
            show_view_query = ("select * from emp_info")
            my_cursor.execute(show_view_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def create_view_with_join(self):
        """
        Description:
            This function will create mysql view with join clause from given columns from table.
        """
        try:
            my_cursor = db_connection.cursor()
            create_view_query ="create view emp_data as select name,salary,dept_name from employee_details inner join department using (department_id)"
            my_cursor.execute(create_view_query)
            logger.info("View created")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def create_view_from_view(self):
        """
        Description:
            This function will create mysql view from previously created view for given columns from table.
        """
        try:
            my_cursor = db_connection.cursor()
            create_view_query ="create view emp_summary as select name,dept_name from emp_data"
            my_cursor.execute(create_view_query)
            logger.info("View created")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def drop_view(self):
        """
        Description:
            This function will drop view.
        """
        try:
            my_cursor = db_connection.cursor()
            drop_view_query ="drop view emp_summary"
            my_cursor.execute(drop_view_query)
            logger.info("View deleted")
        except Exception as e:
            logger.info(f"Errorr!!{e}")


view_object = MysqlViews()
view_object.create_view()
view_object.display_view()
view_object.update_view()
view_object.display_updated_view()
view_object.create_view_with_join()
view_object.create_view_from_view()
view_object.drop_view()