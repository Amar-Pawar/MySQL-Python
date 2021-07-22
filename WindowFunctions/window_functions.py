'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-21
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-22
@Title : Program for MySQL window functions
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

class WindowFunction():

    def create_table(self):
        """
        Description:
            This function will create a new table.
        """
        try:
            my_cursor = db_connection.cursor()
            query = "create table emp_sales(id int primary key not null,name varchar(20),year int not null,country varchar(20), product varchar(45), sale int not null)"
            my_cursor.execute(query)
            logger.info("table crated")
        except Exception as e:
            logger.info(f"error{e}")

window_obj = WindowFunction()
window_obj.create_table()