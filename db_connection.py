# db_connection.py

import pymysql
from pymysql import Error
from config import Config

class DatabaseConnection:
    def __init__(self):
        self.config = Config.DATABASE_CONFIG
        self.connection = None

    def connect(self):
        try:
            print(self.config)
            self.connection = pymysql.connect(**self.config)
            if self.connection.open:
                print("数据库连接成功")
        except Error as e:
            print(f"Error: {e}")
            raise

    def get_cursor(self):
        return self.connection.cursor(pymysql.cursors.DictCursor)

    def close(self):
        if self.connection and self.connection.open:
            self.connection.close()
            print("数据库连接已关闭")