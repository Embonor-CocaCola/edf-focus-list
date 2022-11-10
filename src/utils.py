import os

def getRawSql(filename):
    sql_path = os.path.join(os.path.dirname(__file__), 'sql', filename)
    return open(sql_path, 'r').read()

def formatValidation():
    print('Hola')