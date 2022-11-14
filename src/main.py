from db import DB
from utils import getRawSql, getPath

db = DB()

def createTempTable():
    db.query(getRawSql('create_temp_table.sql'))

def loadProcess():
    db.copy(getRawSql('load_csv_into_temp.sql'), open(getPath("../data/focus_list.csv"), "r"))

def softDeleteProcess():
    db.query(getRawSql('soft_delete.sql'))

def typedProcess():
    db.query(getRawSql('typed_data.sql'))

def dropTempTable():
    db.query(getRawSql('drop_temp_table.sql'))

def exportErrors():
    # db.copy(getRawSql('export_edf_subtype_error.sql'), open(getPath("../logs/edf_subtype_error.csv"), 'w', encoding='UTF8'))
    db.copy(getRawSql('export_customer_error.sql'), open(getPath("../logs/customer_error.csv"), 'w', encoding='UTF8'))

def main():
    createTempTable()
    loadProcess()
    softDeleteProcess()
    typedProcess()
    exportErrors()
    dropTempTable()

if __name__ == '__main__':
    main()