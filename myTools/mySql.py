# Coding : utf-8
# Author : chyh
# Date   : 2021/2/14 0:11


import pymysql


class MyPythonSql:
    conn = pymysql.Connection
    cursor = pymysql.cursors

    def buildConn(self):
        conn = pymysql.connect(host="192.168.52.102", user="root", passwd="123456", db="spider")
        cursor = conn.cursor()
        self.conn = conn
        self.cursor = cursor

    def query(self, sql):
        # print(sql)
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def insert(self, sql):
        # noinspection PyBroadException
        # print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return "insert success"
        except:
            self.conn.rollback()
            return "insert failed"

    def update(self, sql):
        # noinspection PyBroadException
        # print(sql)
        try:
            self.cursor.execute(sql)
            self.conn.commit()
            return "update success"
        except:
            self.conn.rollback()
            return "update failed"

    def close(self):
        self.conn.close()

    def __init__(self):
        self.buildConn()
