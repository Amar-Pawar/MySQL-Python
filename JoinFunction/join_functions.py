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

join_object = JoinFunction()
join_object.inner_join()


