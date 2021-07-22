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

    def insert_values(self):
        """
        Description:
            This function will insert vakues in table.
        """
        try:
            my_cursor = db_connection.cursor()
            query = '''insert into emp_sales(id,name,year,country, product, sale) values 
                    (1,'Amar',2019,'India','iphone10',40000),
                    (2,'Sagar',2021,'US','iphone12',80000),
                    (3,'Nishad',2018,'US','iphone8',30000),
                    (4,'Mayur',2020,'India','iphone11',50000),
                    (5,'Sanket',2020,'UK','iphone11',50000),
                    (6,'Swaraj',2021,'UK','iphone12',80000)'''
            my_cursor.execute(query)
            db_connection.commit()
            logger.info(f"Data inserted: {my_cursor}")
        except Exception as e:
            logger.info(f"error{e}")

    def window_aggregate_function(self):
        """
        Description:
            This function will give sum of sale based on given condition with window function.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("select year,product,sale,sum(sale) over(partition by year) as total_sale from emp_sales")
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    # Window analytical functions
    def window_analytical_ntile(self):
        """
        Description:
            This function will sort rows in given numbers in ntile() function.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("select year,product,sale, Ntile(4) over() as total_sale from emp_sales")
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def window_analytical_lead(self):
        """
        Description:
            This function will read data from next row in given condition in query.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("select year, product,sale, lead(sale,1) over(order by year) as total_sale from emp_sales")
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    # Window ranking functions
    def window_dense_rank(self):
        """
        Description:
            This function will give dense rank for given column in condition.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("select year, product,sale, dense_rank() over(partition by year order by sale) as 'dense_rank' from emp_sales")
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def window_rank(self):
        """
        Description:
            This function will given ranks for specified column in query.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("select year, product,sale, rank() over(partition by year order by sale desc) as 'rank' from emp_sales")
            result = my_cursor.fetchall()
            logger.info(result)
        except Exception as e:
            logger.info(f"Errorr!!{e}")


window_obj = WindowFunction()
window_obj.create_table()
window_obj.insert_values()
window_obj.window_aggregate_function()
window_obj.window_analytical_ntile()
window_obj.window_analytical_lead()
window_obj.window_dense_rank()
window_obj.window_rank()