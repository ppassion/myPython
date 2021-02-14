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
    contents = generatePostContents()
    processPostContents(contents)


def getPageLinks():
    url = baseUrl + "forum.php?mod=forumdisplay&fid=45"
    html = askUrl(url)
    soup = BeautifulSoup(html, "html.parser")
    findPageCount = re.compile(r'<span title="共(.*?)页"')
    pageCount = re.findall(findPageCount, str(soup))
    pageCount = int(pageCount[0].strip())
    pageLinks = []
    for i in range(0, pageCount):
        link = baseUrl + "forum.php?mod=forumdisplay&fid=45&page=" + str(i + 1)
        pageLinks.append(link)
    return pageLinks


def generatePostContents():
    contents = []
    postUrl = "http://www.xiaohonglouss.com/forum.php?mod=viewthread&tid="
    for i in range(102898, 102899):
        # for i in range(1, 5):
        url = postUrl + str(i)
        html = askUrl(url)
        soup = BeautifulSoup(html, "html.parser")
        contents.append(soup)
    return contents


def processPostContents(contents):
    for content in contents:
        # print(content)
        findExistFlag = re.compile(r'指定的主题不存在或已被删除或正在被审核')
        existFlag = re.findall(findExistFlag, str(content))
        if len(existFlag) >= 1:
            print(existFlag)
        else:
            getInfo(str(content))
            getImg(content)


def getImg(soup):
    imgList = []
    for item in soup.find_all("img", class_="zoom"):
        file = item['file']
        imgLink = baseUrl + file
        imgList.append(imgLink)
    for imgLink in imgList:
        request.urlretrieve(imgLink, "picture1.jpg")
    return imgList


def getInfo(content):
    postInfo = {}

    # title
    findTitle = re.compile(r'<span id="thread_subject">(.*?)</span>')
    title = re.findall(findTitle, content)
    print(title)
    postInfo["title"] = title

    # date
    findDate = re.compile(r'【验证时间】：(.*)<br/>')
    date = re.findall(findDate, content)
    print(date)
    postInfo["date"] = date

    # location
    findLocation = re.compile(r'【验证地点】：(.*)<br/>')
    location = re.findall(findLocation, content)
    print(location)
    postInfo["location"] = location

    # env
    findEnv = re.compile(r'【环境设备】：(.*)<br/>')
    env = re.findall(findEnv, content)
    print(env)
    postInfo["env"] = env

    # price
    findPrice = re.compile(r'【价格一览】：(.*)<br/>')
    price = re.findall(findPrice, content)
    print(price)
    postInfo["price"] = price

    # key
    findKey = re.compile(r'【重点推荐】：(.*)<br/>')
    key = re.findall(findKey, content)
    print(key)
    postInfo["key"] = key

    # detail
    findDetail = re.compile(r'【验证细节】：(.*)<br/>')
    detail = re.findall(findDetail, content)
    print(detail)
    postInfo["detail"] = detail

    print("=================================================")
    return postInfo


if __name__ == '__main__':
    getData()
