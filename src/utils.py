import os
import csv
from pathlib import Path


def get_raw_sql(filename):
    sql_path = os.path.join(os.path.dirname(__file__), 'sql', filename)
    return open(sql_path, 'r').read()

def get_path(path):
    return Path(__file__).parent / path

def format_validation():
    pass

def error_file_generator(code, error):
    with open(get_path("../logs/errors.csv"), 'w+') as error_file:
        error_file.write('error_code,error_message\n')
        error_file.write(f'{code},{error}')
        error_file.close()