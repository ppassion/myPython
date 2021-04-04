# Coding : utf-8
# Author : chyh
# Date   : 2021/3/8 21:01

from common.setting import database_info
from spider.proxy.src.log.logger import logger

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import sqlite3


class database_opt:

    def __init__(self) -> None:
        engine = create_engine('sqlite:///proxy.db?check_same_thread=False', echo=True)
        self.db_session = sessionmaker(bind=engine)

    def add_proxy(self, new_proxy):
        session = self.db_session()
        session.add(new_proxy)
        try:
            session.commit()
        except IntegrityError as e:
            logger.warning(new_proxy.ip + ':' + new_proxy.port + "已存在")
        finally:
            session.close()

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
