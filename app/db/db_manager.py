import psycopg2
import psycopg2.extras as extra
from app import app
from pprint import pprint
from codecs import open
import os


class DBConnection:
    def __init__(self):
        try:
            if os.environ["APP_SETTINGS"] == "TESTING":
                self.con = psycopg2.connect(
                    database="store_manager_testing", user="postgres", password="araali", host="localhost", port="5432")
            else:
                self.con = psycopg2.connect(
                    database="d80u6f4o43aan7", user="srzjrqwazxzwta", password="4d7d7419d4f7b372cd3623e7196e0b32b60daca7a07e5094b4f8478fbe8c155b", host="ec2-107-21-233-72.compute-1.amazonaws.com", port="5432")
            self.con.autocommit = True
            self.dict_cursor = self.con.cursor(
                cursor_factory=extra.RealDictCursor)
        except Exception as ex:
            pprint("Database connection error: "+str(ex))

    def create_tables(self):
        create_users_table = open(
            'app/db/create_users.sql', mode='r', encoding='utf-8-sig').read()
        create_products_table = open(
            'app/db/create_products.sql', mode='r', encoding='utf-8-sig').read()
        create_sales_table = open(
            'app/db/create_sales.sql', mode='r', encoding='utf-8-sig').read()
        queries = (create_users_table,
                   create_products_table, create_sales_table)

        # try:
        for query in queries:
            self.dict_cursor.execute(query)
        # except Exception as ex:
        #     pprint("Table creation error: "+str(ex))    

    def delete_tables(self):
        delete_queries = (
            """
            DROP TABLE IF EXISTS users CASCADE
            """,
            """
			DROP TABLE IF EXISTS products CASCADE
			""",
            """
            DROP TABLE IF EXISTS sales CASCADE
            """)
        for query in delete_queries:
            self.dict_cursor.execute(query)
