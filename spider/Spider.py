# coding: utf-8
# Author：chyh
# Date ：2021/2/4 11:28


from bs4 import BeautifulSoup
import re
import urllib
import xlwt
import sqlite3
import urllib
from urllib import request, parse

baseUrl = "https://movie.douban.com/top250?start="
savePath = ".\\top250,xlsx"


def getData():
    dataList = []
    for i in range(0, 10):
        url = baseUrl + str(i * 25)
        html = askUrl(url)
        dataList.append(html)
    return dataList


def saveData(path):
    return 1


def askUrl(url):
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.104 Safari/537.36 "
    }
    data = bytes(parse.urlencode({"hello": "world"}), encoding="utf-8")
    req = request.Request(url, data=data, headers=header, method="GET")
    try:
        response = request.urlopen(req)
    except urllib.error.URLError as e:
        print(e.code)
    return response


if __name__ == '__main__':
    # getData()
    print(getData())
