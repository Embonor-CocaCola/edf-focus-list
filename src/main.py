from db import DB
import logging
from pathlib import Path
from utils import getRawSql

db = DB()

def createTempTable():
    db.query(getRawSql('create_temp_table.sql'))

def loadProcess():
    path = Path(__file__).parent / "../data/focus_list.csv"
    db.copy(getRawSql('load_csv_into_temp.sql'), open(path, "r"))

def softDeleteProcess():
    db.query(getRawSql('soft_delete.sql'))

def typedProcess():
    db.query(getRawSql('typed_data.sql'))

def dropTempTable():
    db.query(getRawSql('drop_temp_table.sql'))

def exportNonExistingCustomers():
    path = Path(__file__).parent / "../logs/customer_error.csv"
    db.copy(getRawSql('export_errors.sql'), open(path, 'w', encoding='UTF8'))

def main():
    createTempTable()
    loadProcess()
    softDeleteProcess()
    typedProcess()
    exportNonExistingCustomers()
    dropTempTable()

if __name__ == '__main__':
    main()