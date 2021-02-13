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
    for i in range(0, 1):
        url = baseUrl + str(i * 25)
        html = askUrl(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            item = str(item)
            getInfo(item)


def getInfo(item):
    # title
    findTitle = re.compile(r'<span class="title">(.*?)</span>')
    title = re.findall(findTitle, item)
    print(title)

    # link
    findLink = re.compile(r'<a href="(.*?)">')
    link = re.findall(findLink, item)
    print(link)

    # img
    findImg = re.compile(r'<img.*src="(.*?)"')
    img = re.findall(findImg, item)
    print(img)

    # rating
    findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
    rating = re.findall(findRating, item)
    print(rating)

    # people
    findPeople = re.compile(r'<span>(\d*人评价)</span>')
    people = re.findall(findPeople, item)
    print(people)

    print("=================================================")


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
    getData()
    # print(len(getData()))
