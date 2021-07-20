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

    def show_database(self):
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

    def show_tables(self):
        """
        Description:
            This function shows all the tables present in database with given query.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("show tables")
            for i in my_cursor:
                logger.info(i)
        except Exception as e:
            logger.info(f"Errorr!!{e}")
        
    def read_tables(self):
        """
        Description:
            This function will read all the information in table in database with given query.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("select * from student_info")
            for i in my_cursor:
                logger.info(i)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def create_table(self):
        """
        Description:
            This function will create table in given database.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("create table employee_details(id int(4) auto_increment primary key not null, employee_name varchar(15),salary int(5))")
            logger.info(f"Table created {my_cursor}")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def insert_data(self):
        """
        Description:
            This function will insert data into table with given query.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("insert into employee_details(employee_name,salary) values ('Mayur','40000'),('Amar', '50000')")
            db_connection.commit()
            logger.info(f"Data inserted: {my_cursor}")
        except Exception as e:
            logger.info(f"Errorr!!{e}")
    def read_employee_table(self):
            """
            Description:
                This function will read all the information in table in database with given query.
            """
            try:
                my_cursor = db_connection.cursor()
                my_cursor.execute("select * from employee_details")
                for i in my_cursor:
                    logger.info(i)
            except Exception as e:
                logger.info(f"Errorr!!{e}")

    def alter_table(self):
        """
        Description:
            This function will alter the table and add column gender to it.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("alter table employee_details ADD column gender varchar(10) after employee_name")
            db_connection.commit()
            logger.info(f"column added")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def update_table(self):
        """
        Description:
            This function will update the column inside table.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("update employee_details set gender='M' where employee_name='Mayur'")
            db_connection.commit()
            logger.info("Record updated")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def delet_record(self):
        """
        Description:
            This function will delete the entry from table.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("delete from employee_details where employee_name='Amar'")
            db_connection.commit()
            logger.info("Record deleted")
        except Exception as e:
            logger.info(f"Errorr!!{e}")

 
operations = CrudOperations()
operations.show_database()
operations.show_tables()
operations.read_tables()
operations.create_table()
operations.insert_data()
operations.read_employee_table()
operations.alter_table()
operations.update_table()
operations.delet_record()