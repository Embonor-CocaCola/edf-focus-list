import psycopg2
from connection import Connection
from utils import error_file_generator

class DB():
    def __init__(self):
        self.conn = Connection()
        self.cur = self.conn.cur

    def query(self, query, item=None):
        if self.conn is not None:
            try:
                if item is not None:
                    self.cur.execute(query, item)
                else:
                    self.cur.execute(query)
                self.conn.commit()
            except psycopg2.Error as error:
                error_file_generator(error.pgcode, error.pgerror)
                raise error
            finally:
                print(f'Query executed successfully.')

    def find_all(self, query):
        if self.conn is not None:
            try:
                self.cur.execute(query)
                return self.cur.fetchall()
            except psycopg2.Error as error:
                error_file_generator(error.pgcode, error.pgerror)
                raise error
            finally:
                print(f'FindAll executed successfully.')

    def find(self, query):
        if self.conn is not None:
            try:
                self.cur.execute(query)
                return self.cur.fetchone()
            except psycopg2.Error as error:
                error_file_generator(error.pgcode, error.pgerror)
                raise error
            finally:
                print(f'Find executed successfully.')

    def copy(self, query, file): 
        if self.conn is not None:
            try:
                self.cur.copy_expert(query, file)
                self.conn.commit()
            except psycopg2.Error as error:
                error_file_generator(error.pgcode, error.pgerror)
                raise error
            finally:
                print(f'Copy executed successfully.')

    def close(self):
        if self.conn is not None:
            try:
                self.conn.close()
            except psycopg2.Error as error:
                error_file_generator(error.pgcode, error.pgerror)
                raise error
            finally:
                print(f'Connection closed successfully.')