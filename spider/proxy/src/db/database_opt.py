# Coding : utf-8
# Author : chyh
# Date   : 2021/3/8 21:01

from spider.proxy.src.setting import database_info
from spider.proxy.src.db.i_database_opt import i_database_opt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from spider.proxy.src.log.logger import logger
import sqlite3


class database_opt(i_database_opt):

    def __init__(self):
        engine = create_engine('sqlite:///proxy.db')
        self.db_session = sessionmaker(bind=engine)

    def add_proxy(self, proxy):
        pass

    def create_table(self):
        try:
            conn = self.connect_database()
            cursor = conn.cursor()
            logger.info("初始化sqlite数据库")
            cursor.execute(database_info['ddl'])
        except sqlite3.OperationalError:
            logger.error('create table failed')
        finally:
            cursor.close()
            conn.close()

    @staticmethod
    def connect_database():
        return sqlite3.connect(database_info['db_name'])


database_opt = database_opt()
