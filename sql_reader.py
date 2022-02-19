# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 16:42:31 2021

@author: joe.cavarretta
"""

############### IMPORT DEPENDENCIES & SET FORMATS ###############
import pandas as pd
import pyodbc
from datetime import datetime


############### CONNECT TO DB ###############
conn = pyodbc.connect('DRIVER={SQL Server};'                                    # Microsoft SQL server, change if using other server
                      'SERVER=;'
                      'DATABASE=;'
                      'Trusted_Connection=yes;')                                # This line uses your windows login credentials automatically

print(conn)

############### DEFINE READSQL CODE ###############
def readSQL(file_path):
    fd = open(file_path)
    sql = fd.read()
    fd.close()
    return pd.read_sql(sql,conn)

############## RUN SQL QUERY ###############
startTime = datetime.now()
df = readSQL('sql_file_name_here.sql')                                          # Insert SQL file here

print('Data Loaded!')

############### SAVE AS A CSV FILE ###############
df.to_csv('file_name_here.csv', index = False)                                  # name output file here

print('SQL query runtime: {}'.format(datetime.now() - startTime))
