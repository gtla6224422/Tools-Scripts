# config.py
import os

class Config:
    DATABASE_CONFIG = {
        'host': '1.14.155.39',  # 例如'localhost'
        'user': 'wzd',
        'password': 'Wzd123!$&',
        'database': 'web_demo',
        'charset': 'utf8mb4',  # 根据需要设置字符集
    }


    # 使用相对路径指向项目根目录下的outputfile文件夹
    OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputfile')
    
    # 确保目录存在
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)