import psycopg2
from config import (
    DB_CONNECTION_HOST,
    DB_CONNECTION_PORT,
    DB_CONNECTION_DB,
    DB_CONNECTION_USER,
    DB_CONNECTION_PASSWORD
)

class Connection():

    def __init__(self):
        self.host = DB_CONNECTION_HOST
        self.username = DB_CONNECTION_USER
        self.password = DB_CONNECTION_PASSWORD
        self.port = DB_CONNECTION_PORT
        self.dbname = DB_CONNECTION_DB
        self.conn = None

    def open(self):
        if self.conn is None:
            try:
                self.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
                )
            except psycopg2.DatabaseError as error:
                print(error)
                raise error
            finally:
                print(f'Connection opened successfully.')

    def query(self, query, item=None):
        if self.conn is not None:
            cur = self.conn.cursor()
            if item is not None:
                cur.execute(query, item)
            else:
                cur.execute(query)
            self.conn.commit()

    def findAll(self, query):
        if self.conn is not None:
            try:
                cur = self.conn.cursor()
                cur.execute(query)
                data = cur.fetchall()
                return data
            except psycopg2.DatabaseError as error:
                print(error)
                raise error
            finally:
                print(f'Connection opened successfully.')

    def find(self, query):
        if self.conn is not None:
            try:
                cur = self.conn.cursor()
                cur.execute(query)
                data = cur.fetchone()
                return data[0]
            except psycopg2.DatabaseError as error:
                print(error)
                raise error
            finally:
                print(f'Connection opened successfully.')

    def close(self):
        if self.conn is not None:
            try:
                self.conn.close()
            except psycopg2.DatabaseError as error:
                print(error)
                raise error
            finally:
                print(f'Connection closed successfully.')