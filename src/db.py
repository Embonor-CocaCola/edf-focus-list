from connection import Connection
import psycopg2

class DB(Connection):
    def __init__(self):
        Connection.__init__(self)

    @staticmethod
    def query(query, item=None):
        if Connection.conn is not None:
            try:
                if item is not None:
                    Connection.cur.execute(query, item)
                else:
                    Connection.cur.execute(query)
                Connection.conn.commit()
            except psycopg2.DatabaseError as error:
                print(error)
                raise error
            finally:
                print(f'Query executed successfully.')

    @staticmethod
    def findAll(query):
        if Connection.conn is not None:
            try:
                cur = Connection.cur
                cur.execute(query)
                data = cur.fetchall()
                return data
            except psycopg2.DatabaseError as error:
                raise error
            finally:
                print(f'FindAll executed successfully.')

    @staticmethod
    def find(query):
        if Connection.conn is not None:
            try:
                cur = Connection.cur
                cur.execute(query)
                return cur.fetchone()
            except psycopg2.DatabaseError as error:
                print(error)
                raise error
            finally:
                print(f'Find executed successfully.')

    @staticmethod
    def copy(query, file): 
        if Connection.conn is not None:
            try:
                cur = Connection.cur
                cur.copy_expert(query, file)
                Connection.conn.commit()
            except psycopg2.DatabaseError as error:
                print(error)
                raise error
            finally:
                print(f'Copy executed successfully.')

    @staticmethod
    def close():
        if Connection.conn is not None:
            try:
                Connection.close()
            except psycopg2.DatabaseError as error:
                print(error)
                raise error
            finally:
                print(f'Connection closed successfully.')