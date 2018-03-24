#!/usr/bin/python

# cvs to mysql db

import MySQLdb as mdb
import csv
import logging

def storeFunction():
    con = mdb.connect('localhost', \
                    'db_user', \
                    'db_password', \
                    'db_name');

    try:
     cur = con.cursor()
     cur.execute(line_to_insert)
     con.commit()


    except mdb.Error, e:
     logger.error(e)

    finally:
     if con:
      con.close()


openFile = open('csv_file_name.csv', 'r')
csvFile = csv.reader(openFile)
header = next(csvFile)
headers = map((lambda x: '`'+x+'`'), header)
insert = 'INSERT INTO db_table_name (' + ", ".join(headers) + ") VALUES "
for row in csvFile:
    values = map((lambda x: '"'+x+'"'), row)
    line_to_insert = (insert +"("+ ", ".join(values) +");" )
    storeFunction()
openFile.close()
