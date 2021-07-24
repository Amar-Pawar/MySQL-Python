'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-07-23
@Last Modified by: Amar Pawar
@Last Modified time: 2021-07-23
@Title : Program to import and export database.
/**********************************************************************************
'''
from re import sub
import sys
sys.path.insert(0, '/home/ubuntu/Documents/PythonWorkspace/MySQL-Operations')
from CrudOperations.logging_handler import logger
import mysql.connector
import os
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

db_connection = mysql.connector.connect(
     host = os.environ.get("DB_HOST"),
     user = os.environ.get("DB_USER"),
     passwd= os.environ.get("DB_PASSWORD"),
     auth_plugin = os.environ.get("AUTH_PLUGIN"),
     database = os.environ.get("DATABASE")
    )
#importing csv file and converting it into pandas dataframe
data = pd.read_csv (r'us_data.csv')   
df = pd.DataFrame(data, columns= ['Rank','State','Postal','Population'])
logger.info(df)

class ImportExport():

    def export_database(self):
        """
        Description:
            This function will export the database in given file.
        """
        try:
            os.system('mysqldump -u root employee > data-dump.sql')
            logger.info("Exporting done")
        except Exception as e:
            logger.info(f"error!!{e}")

    def import_database(self):
        """
        Description:
            This function will import database from given file.
        """
        try:
            my_cursor = db_connection.cursor()
            os.system('mysql -u root  emp_information < data-dump.sql')
            logger.info("importing done")
            my_cursor.execute("show databases")
            db_connection.commit()
        except Exception as e:
            logger.info(f"error!!{e}")

    def show_tables(self):
        """
        Description:
            This function will show tables from imported database.
        """
        try:
            my_cursor = db_connection.cursor()
            my_cursor.execute("show tables")
            for i in my_cursor:
                logger.info(i)
        except Exception as e:
            logger.info(f"Errorr!!{e}")

    def create_table():
        """
        Description:
            This function will create a new table.
        """
        try:
            my_cursor = db_connection.cursor()
            query = "create table us_info(rank_id int primary key not null,state_name varchar(20),postal varchar(20),population int)"
            my_cursor.execute(query)
            logger.info("table crated")
        except Exception as e:
            logger.info(f"error{e}")

    def import_from_csv(self):
        """
        Description:
            This function will import data from csv file and conver it into mysql database table.
        """
        try: 
            my_cursor = db_connection.cursor()
            for row in df.itertuples():
                my_cursor.execute('''INSERT INTO us_info(rank_id,state_name,postal,population)
                            VALUES (%s,%s,%s,%s)''',
                            (row.Rank, 
                            row.State,
                            row.Postal,
                            row.Population)
                            )
            db_connection.commit()
        except Exception as e:
            logger.info(f"Error!!{e}")

import_export_obj = ImportExport()
import_export_obj.export_database()
import_export_obj.import_database()
import_export_obj.show_tables()
import_export_obj.create_table()
import_export_obj.import_from_csv()
