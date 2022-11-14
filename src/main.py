from db import DB
from utils import get_raw_sql, get_path

db = DB()

def create_temp_table():
    sql = get_raw_sql('create_temp_table.sql')
    db.query(sql)

def load_process():
    path = get_path("../data/focus_list.csv")
    with open(path) as csv:
        sql = get_raw_sql('load_csv_into_temp.sql')
        db.copy(sql, csv)

def clean_data():
    sql = get_raw_sql('clean_data.sql')
    db.query(sql)

def soft_delete_process():
    sql = get_raw_sql('soft_delete.sql')
    db.query(sql)

def typed_process():
    sql = get_raw_sql('target_data.sql')
    db.query(sql)

def drop_temp_table():
    sql = get_raw_sql('drop_temp_table.sql')
    db.query(sql)

def export_errors():
    path_customers = get_path("../logs/customer_error.csv")
    # path_edf_subtypes = get_path("../logs/edf_subtype_error.csv")
    sql_customers = get_raw_sql('export_customer_error.sql')
    # sql_edf_subtypes = get_raw_sql('export_edf_subtype_error.sql')

    with open(path_customers) as csv_customers:
        db.copy(sql_customers, csv_customers, 'w', encoding='UTF8')

    # with open(path_edf_subtypes) as csv_subtypes:
    #     db.copy(sql_edf_subtypes, csv_subtypes, 'w', encoding='UTF8')

def main():
    create_temp_table()
    load_process()
    clean_data()
    soft_delete_process()
    typed_process()
    export_errors()
    drop_temp_table()

if __name__ == '__main__':
    main()