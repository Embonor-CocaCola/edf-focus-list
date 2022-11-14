import psycopg2
from config import (
    DB_CONNECTION_HOST,
    DB_CONNECTION_PORT,
    DB_CONNECTION_DB,
    DB_CONNECTION_USER,
    DB_CONNECTION_PASSWORD
)
from utils import error_file_generator

class Connection:
    conn = None

    def __init__(self):
        self.host = DB_CONNECTION_HOST
        self.username = DB_CONNECTION_USER
        self.password = DB_CONNECTION_PASSWORD
        self.port = DB_CONNECTION_PORT
        self.dbname = DB_CONNECTION_DB

        if Connection.conn is None:
            try:
                Connection.conn = psycopg2.connect(
                    host=self.host,
                    user=self.username,
                    password=self.password,
                    port=self.port,
                    dbname=self.dbname
                )
                Connection.cur = self.conn.cursor()
            except psycopg2.Error as error:
                error_file_generator(error.pgcode, error.pgerror)
                raise error
        else:
            raise ConnectionError("You cannot create another Connection class")

    @staticmethod
    def commit():
        if Connection.conn is not None:
            try:
                Connection.conn.commit()
            except psycopg2.Error as error:
                error_file_generator(error.pgcode, error.pgerror)
                raise error

    @staticmethod
    def close():
        if Connection.conn is not None:
            try:
                Connection.conn.close()
                Connection.conn = None
            except psycopg2.Error as error:
                error_file_generator(error.pgcode, error.pgerror)
                raise ConnectionError(error)