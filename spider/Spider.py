# coding: utf-8
# Author：chyh
# Date ：2021/2/4 11:28
import sqlite3

from bs4 import BeautifulSoup
import re
import xlwt
import urllib
from urllib import request, parse

baseUrl = "https://movie.douban.com/top250?start="
savePath = ".\\files\\top250.xls"
dataList = []


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


def getData():
    for i in range(0, 1):
        url = baseUrl + str(i * 25)
        html = askUrl(url)
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all("div", class_="item"):
            item = str(item)
            filmInfo = getInfo(item)
            dataList.append(filmInfo)


def getInfo(item):
    filmInfo = {}
    # title
    findTitle = re.compile(r'<span class="title">(.*?)</span>')
    title = re.findall(findTitle, item)
    # print(title)
    filmInfo["title"] = title

    # link
    findLink = re.compile(r'<a href="(.*?)">')
    link = re.findall(findLink, item)
    # print(link)
    filmInfo["link"] = link

    # img
    findImg = re.compile(r'<img.*src="(.*?)"')
    img = re.findall(findImg, item)
    # print(img)
    filmInfo["img"] = img

    # rating
    findRating = re.compile(r'<span class="rating_num" property="v:average">(.*?)</span>')
    rating = re.findall(findRating, item)
    # print(rating)
    filmInfo["rating"] = rating

    # people
    findPeople = re.compile(r'<span>(\d*人评价)</span>')
    people = re.findall(findPeople, item)
    # print(people)
    filmInfo["people"] = people

    # print("=================================================")
    return filmInfo


def saveDataToExcel():
    workBook = xlwt.Workbook(encoding="utf-8")

    workSheet1 = workBook.add_sheet("top250")

    col = ("title", "link", "img", "rating", "people")
    for i in range(0, 5):
        workSheet1.write(0, i, col[i])
    for i in range(0, 25):
        filmInfo = dataList[i]
        for j in range(0, 5):
            workSheet1.write(i + 1, j, filmInfo[col[j]])
    workBook.save(savePath)


def saveDataToSqlLite():
    conn = sqlite3.connect(".\\files\\test.db")
    print("sss")


if __name__ == '__main__':
    # getData()
    # saveDataToExcel()
    saveDataToSqlLite()
