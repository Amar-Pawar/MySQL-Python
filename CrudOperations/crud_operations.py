'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-19
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-019
@Title : Program to perform various CRUD operations of database
/**********************************************************************************
'''
from logging_handler import logger
import mysql.connector

# setting up the connection
db_connection = mysql.connector.connect(
     host = 'localhost',
     user = 'root',
     passwd= '',
     auth_plugin = 'mysql_native_password',
     database = 'student'
    )

class CrudOperations():

    def read_database(self):
        """
        Description:
            This function shows all the databases present with given query.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("show databases")
            for i in my_cursor:
                logger.info(i)
        except Exception as e:
            logger.info(f"Errorr!!{e}")
    
operations = CrudOperations()
operations.read_database()