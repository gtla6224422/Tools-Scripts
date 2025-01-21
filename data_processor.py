# data_processor.py

import pandas as pd
from db_connection import DatabaseConnection
import os
from config import Config

class DataProcessor:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def fetch_orders(self):
        query = "SELECT order_id FROM order_tbl WHERE order_cost > 800"
        
        cursor = self.db_connection.get_cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        df = pd.DataFrame(results)

        # 确保输出目录存在
        output_dir = os.path.dirname(Config.OUTPUT_PATH)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"创建目录: {output_dir}")

        # 将数据写入Excel文件
        df.to_excel(Config.OUTPUT_PATH, index=False, engine='openpyxl')
        print(f"数据已成功导出到{Config.OUTPUT_PATH}")

        cursor.close()

def run():
    # 初始化数据库连接
    db_connection = DatabaseConnection()
    db_connection.connect()

    # 使用数据库连接实例化数据处理器
    data_processor = DataProcessor(db_connection)

    # 执行查询并导出数据
    data_processor.fetch_orders()

    # 关闭数据库连接
    db_connection.close()