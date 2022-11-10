from db import DB
from pathlib import Path
import csv
import logging
import time
import psycopg2
from utils import getRawSql

db = DB()

def createTempTable():
    db.query(getRawSql('create_temp_table.sql'))
    print('Algo 1')

def loadProcess():
    path = Path(__file__).parent / "../data/focus_list.csv"
    db.copy(getRawSql('load_csv_into_temp.sql'), open(path, "r"))
    print('Algo 2')

def typedProcess():
    db.query(getRawSql('typed_data.sql'))
    print('Algo 3')
    # db.close()

def softDeleteProcess():
    db.query(getRawSql('soft_delete.sql'))
    print('Algo 4')

def main():
    createTempTable()
    loadProcess()
    # softDeleteProcess()
    typedProcess()

if __name__ == '__main__':
    main()
    test = DB()
    print(test.conn)