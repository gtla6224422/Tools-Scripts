# data_processor.py

import pandas as pd
from db_connection import DatabaseConnection
import os
from config import Config
from datetime import datetime

class DataProcessor:
    def __init__(self, db_connection):
        self.db_connection = db_connection

    def fetch_orders(self):
        query = "SELECT order_id FROM order_tbl WHERE order_cost > 800"
        
        cursor = self.db_connection.get_cursor()
        cursor.execute(query)
        results = cursor.fetchall()

        df = pd.DataFrame(results)

        # 获取当前时间并格式化为字符串
        current_time = datetime.now().strftime('%Y%m%d%H%M')
        file_name = f'order_{current_time}.xlsx'

        # 完整的文件路径
        output_path = os.path.join(Config.OUTPUT_DIR, file_name)

        # 确保输出目录存在
        if not os.path.exists(Config.OUTPUT_DIR):
            os.makedirs(Config.OUTPUT_DIR)
            print(f"创建目录: {Config.OUTPUT_DIR}")

        # 将数据写入Excel文件
        df.to_excel(output_path, index=False, engine='openpyxl')
        print(f"数据已成功导出到{output_path}")

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