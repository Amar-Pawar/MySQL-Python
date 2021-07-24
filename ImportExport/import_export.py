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

import_export_obj = ImportExport()
import_export_obj.export_database()
