# Coding : utf-8
# Author : chyh
# Date   : 2021/3/8 21:01

from spider.proxy.src.setting import database_info
from spider.proxy.src.db.IDbOpt import IDbOpt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from spider.proxy.src.log.logger import logger
import sqlite3


class DbOpt(IDbOpt):

    def __init__(self):
        engine = create_engine('sqlite:///proxy.db')
        self.db_session = sessionmaker(bind=engine)

    def add_proxy(self, proxy):
        pass

    def create_table(self):
        conn = self.connect_database()
        cursor = conn.cursor()
        try:
            cursor.execute(database_info['ddl'])
        except sqlite3.OperationalError:
            logger.warn('create table failed')
        finally:
            cursor.close()
            conn.close()


    @staticmethod
    def connect_database():
        return sqlite3.connect(database_info['db_name'])


dbOpt = DbOpt()
