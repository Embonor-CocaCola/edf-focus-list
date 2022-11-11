from db import DB
from pathlib import Path
import logging
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

def main():
    createTempTable()
    loadProcess()
    softDeleteProcess()
    typedProcess()
    dropTempTable()

if __name__ == '__main__':
    main()