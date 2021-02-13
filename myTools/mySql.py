# Coding : utf-8
# Author : chyh
# Date   : 2021/2/14 0:11


import pymysql


class MyPythonSql:
    conn = pymysql.Connection
    cursor = pymysql.cursors

    def buildConn(self):
        conn = pymysql.connect(host="192.168.52.102", user="root", passwd="123456", db="bigdata")
        self.conn = conn
        cursor = conn.cursor()
        self.cursor = cursor

    def query(self, sql):
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def __init__(self):
        self.buildConn()
