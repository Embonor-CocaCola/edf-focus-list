import os
import csv
from pathlib import Path


def getRawSql(filename):
    sql_path = os.path.join(os.path.dirname(__file__), 'sql', filename)
    return open(sql_path, 'r').read()

def getPath(path):
    return Path(__file__).parent / path

def formatValidation():
    pass

def errorFileGenerator(code, error):
    with open(getPath("../logs/errors.csv"), 'w+') as error_file:
        error_file.write('error_code,error_message\n')
        error_file.write(f'{code},{error}')
        error_file.close()