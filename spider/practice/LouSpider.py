# coding: utf-8
# Author：chyh
# Date ：2021/2/4 11:28
import sqlite3

from bs4 import BeautifulSoup
import re
import xlwt
import urllib
from urllib import request, parse

baseUrl = "http://www.xiaohonglouss.com/"
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
    pageLinks = getPageLinks()
    getPostLinks(pageLinks)


def getPageLinks():
    url = baseUrl + "forum.php?mod=forumdisplay&fid=45"
    html = askUrl(url)
    soup = BeautifulSoup(html, "html.parser")
    findPageCount = re.compile(r'<span title="共(.*?)页"')
    pageCount = re.findall(findPageCount, str(soup))
    pageCount = int(pageCount[0].strip())
    pageLinks = []
    for i in range(0, pageCount):
        link = baseUrl + "forum.php?mod=forumdisplay&fid=45&page=" + str(i+1)
        pageLinks.append(link)
    return pageLinks


def getPostLinks(pageLinks):
    for pageLink in pageLinks:
        html = askUrl(pageLink)

    # for i in range(1, pageCount + 1):
    #     url = baseUrl + "forum.php?mod=forumdisplay&fid=45&page=" + str(i)
    #     html = askUrl(url)
    #     soup = BeautifulSoup(html, "html.parser")
    #     for item in soup.find_all("div", class_="item"):
    #         item = str(item)
    #         filmInfo = getInfo(item)
    #         dataList.append(filmInfo)


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


if __name__ == '__main__':
    aaa = ['http://www.xiaohonglouss.com/forum.php?mod=forumdisplay&fid=45&page=1']
    getPageLinks(aaa)
