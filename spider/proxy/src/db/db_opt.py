# Coding : utf-8
# Author : chyh
# Date   : 2021/3/8 21:01

from spider.proxy.src.db.db_opt_interface import DataBaseOptInterface


class DataBaseOpt(DataBaseOptInterface):

    def add_proxy(self, proxy):
        pass


sqlite_opt = SqliteOpt()
