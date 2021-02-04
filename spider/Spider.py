# coding: utf-8
# Author：chyh
# Date ：2021/2/4 11:28


from bs4 import BeautifulSoup
import re
import urllib
import xlwt
import sqlite3

baseUrl = "https://movie.douban.com/top250?start="
savePath = ".\\top250,xlsx"


def getData(baseUrl):
    dataList = []
    return dataList


def saveData(path):
    return 1


def askUrl(url):
    header = {}


if __name__ == '__main__':
    print("hello spider")
    getData()
