from connection import Connection
from pathlib import Path
import csv
import logging
import time
import psycopg2

def createTempTable():
    db = Connection()
    db.open()
    db.query("""
        DROP TABLE IF EXISTS temp_focus_list;
        CREATE TABLE "temp_focus_list"(
            "customerId" VARCHAR NOT NULL,
            "suggestedEdf" VARCHAR,
            "subtypeName" VARCHAR,
            "subtypeId" VARCHAR
        );
    """)
    db.close()

def extractProcess():
    db = Connection()
    db.open()
    path = Path(__file__).parent / "../data/focus_list.csv"
    with path.open() as f:
        data = list(csv.reader(f))
        print(data)
        data.pop(0)
        for item in data:
            print(item)
            db.query("""INSERT INTO temp_focus_list VALUES (%s, %s, %s, %s);""", item)
    db.close()

def transformAndLoadProcess():
    db = Connection()
    db.open()
    data = db.findAll("""SELECT * FROM temp_focus_list tmp;""")
    # SELECT "customerId", "suggestedEdf", "subtypeName", "subtypeId"  
    # FROM temp_focus_list
    # tmp inner join "EquipmentSubtype" e on tmp."subtypeId"::numeric = e.id;
    with open(f'{Path(__file__).parent / "../logs/error.txt"}', 'w') as error_file:
        error_file.write('customer_id,subtype_id,subtype_name,error_message\n')  # header
        for item in data:
            values = (int(item[0]), item[1], item[2], int(item[3]))
            print(values)
            try:
                db.query("""
                    INSERT INTO public."FocusList"
                    ("customerId", "suggestedEdf", "edfSubType", "edfSubtypeId", "createdAt", "updatedAt")
                    VALUES (%s, %s, %s, %s, now(), now());
                """, values)
                time.sleep(0.1)
            except psycopg2.Error as error:
                print(error)
                error_file.write(f'{item[0]},{item[3]},{item[1]},"{str(error)}"\n')
                print(f'Cannot load info for customer {item[0]}: {str(error)}')


        print(data)
        db.close()

def softDeleteProcess():
    db = Connection()
    db.open()
    count = db.find("""SELECT COUNT(*) FROM public."FocusList";""")
    if count > 0:
        db.query("""
            UPDATE public."FocusList"
            SET "updatedAt" = now(), "deletedAt" = now()
            WHERE "deletedAt" IS NULL;
        """)
    db.close()


def main():
    # createTempTable()
    softDeleteProcess()
    extractProcess()
    transformAndLoadProcess()
if __name__ == '__main__':
    main()
