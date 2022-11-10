import psycopg2
from config import (
    DB_CONNECTION_HOST,
    DB_CONNECTION_PORT,
    DB_CONNECTION_DB,
    DB_CONNECTION_USER,
    DB_CONNECTION_PASSWORD
)

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
                return Connection
            except psycopg2.DatabaseError as error:
                raise error
        else:
            raise ConnectionError("You cannot create another Connection class")

    @staticmethod
    def close():
        if Connection.conn is not None:
            try:
                Connection.conn.close()
                Connection.conn = None
            except psycopg2.DatabaseError as error:
                raise ConnectionError(error)