'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-21
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-21
@Title : Program for MySQL indexes
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

class MysqlIndexes():

    def create_index(self):
        """
        Description:
            This function will create index for particular table.
        """
        try:
            my_cursor = db_connection.cursor()
            create_index_query ="create index salary on employee_details(salary)"
            my_cursor.execute(create_index_query)
            logger.info("Index for given table created")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def show_index(self):
        """
        Description:
            This function will show indexes.
        """
        try:
            my_cursor = db_connection.cursor()
            show_index_query ="show indexes from employee_details"
            my_cursor.execute(show_index_query)
            result = my_cursor.fetchall()
            logger.info(f"Information as below {result}")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def explain_index(self):
        """
        Description:
            This function will retrieve data with index.
        """
        try:
            my_cursor = db_connection.cursor()
            explain_index_query ="explain select * from employee_details where salary = '30000'"
            my_cursor.execute(explain_index_query)
            result = my_cursor.fetchall()
            logger.info(f"Information as below {result}")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def retrieve_by_index(self):
        """
        Description:
            This function will retrieve data with index.
        """
        try:
            my_cursor = db_connection.cursor()
            retrieve_data_query ="select * from employee_details where salary = '30000'"
            my_cursor.execute(retrieve_data_query)
            result = my_cursor.fetchall()
            logger.info(f"Information as below {result}")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def update_by_index(self):
        """
        Description:
            This function will update data with index.
        """
        try:
            my_cursor = db_connection.cursor()
            update_data_query ="update employee_details set salary ='70000' where name = 'Mayur'"
            my_cursor.execute(update_data_query)
            db_connection.commit()
            logger.info("record updated")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def show_data(self):
        """
        Description:
            This function will retrieve data.
        """
        try:
            my_cursor = db_connection.cursor()
            show_data_query ="select * from employee_details"
            my_cursor.execute(show_data_query)
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def delete_data(self):
        """
        Description:
            This function will delete data from table.
        """
        try:
            my_cursor = db_connection.cursor()
            delete_data_query ="delete from employee_details where name='Nishad'"
            my_cursor.execute(delete_data_query)
            db_connection.commit()
            logger.info("Record deleted")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def drop_index(self):
        """
        Description:
            This function will drop index.
        """
        try:
            my_cursor = db_connection.cursor()
            drop_index_query ="drop index salary on employee_details"
            my_cursor.execute(drop_index_query)
            db_connection.commit()
            logger.info("Index dropped!!")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

index_obj = MysqlIndexes()
index_obj.create_index()
index_obj.show_index()
index_obj.explain_index()
index_obj.retrieve_by_index()
index_obj.update_by_index()
index_obj.show_data()
index_obj.delete_data()
index_obj.drop_index()