# coding: utf-8
# Author：chyh
# Date ：2021/2/4 11:28
import sqlite3

from bs4 import BeautifulSoup
import re
import urllib
from urllib import request, parse
from myTools import mySql
import os

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
    # contents = generatePostContents()
    # processPostContents(contents)
    # pageLinks = getPageLinks()
    # getPostLinks(pageLinks)
    # generatePostContents()
    getPostContents()


def getPageLinks():
    url = baseUrl + "forum.php?mod=forumdisplay&fid=45"
    html = askUrl(url)
    soup = BeautifulSoup(html, "html.parser")
    findPageCount = re.compile(r'<span title="共(.*?)页"')
    pageCount = re.findall(findPageCount, str(soup))
    pageCount = int(pageCount[0].strip())
    pageLinks = []
    for i in range(0, 2):
        link = baseUrl + "forum.php?mod=forumdisplay&fid=45&page=" + str(i + 1)
        pageLinks.append(link)
    return pageLinks


def getPostLinks(pageLinks):
    postIds = []
    for pageLink in pageLinks:
        html = askUrl(pageLink)
        soup = BeautifulSoup(html, "html.parser")
        findPostId = re.compile(r'<tbody id="normalthread_(.*)">')
        postId = re.findall(findPostId, str(soup))
        postIds.extend(postId)
    print(postIds)
    insertPostIdsToDatabase(postIds)
    return postIds


def insertPostIdsToDatabase(postIds):
    baseSql = "insert into POST_ID values('"
    conn = mySql.MyPythonSql()
    for postId in postIds:
        sql = baseSql + postId + "', '0')"
        conn.insert(sql=sql)
    conn.close()


def getPostContents():
    contents = []
    conn = mySql.MyPythonSql()
    postIds = conn.query("select post_id from POST_ID where is_download = '0' limit 1;")
    conn.close()
    basePostUrl = "http://www.xiaohonglouss.com/forum.php?mod=viewthread&tid="
    for postId in postIds:
        url = basePostUrl + postId[0]
        html = askUrl(url)
        soup = BeautifulSoup(html, "html.parser")
        contents.append([postId[0], soup])
    processPostContents(contents)


def processPostContents(contents):
    for content in contents:
        postId = content[0]
        soup = content[1]
        findExistFlag = re.compile(r'指定的主题不存在或已被删除或正在被审核')
        existFlag = re.findall(findExistFlag, str(soup))
        if len(existFlag) >= 1:
            conn = mySql.MyPythonSql()
            conn.update("update POST_ID set is_download = '2' where post_id = '" + postId + "'")
            conn.close()
        else:
            getInfo(postId, soup)


def getInfo(postId, soup):
    title = getSpecifiedPattern(soup, 'title', r'<span id="thread_subject">(.*?)</span>')
    date = getSpecifiedPattern(soup, 'date', r'【验证时间】：(.*)<br/>')
    location = getSpecifiedPattern(soup, 'location', r'【验证地点】：(.*)<br/>')
    env = getSpecifiedPattern(soup, 'env', r'【环境设备】：(.*)<br/>')
    price = getSpecifiedPattern(soup, 'price', r'【价格一览】：(.*)<br/>')
    key = getSpecifiedPattern(soup, 'key', r'【重点推荐】：(.*)<br/>')
    detail = getSpecifiedPattern(soup, 'detail', r'【验证细节】：(.*)<br/>')


def getSpecifiedPattern(soup, example):
    pattern = re.compile(example)
    founds = re.findall(pattern, str(soup))
    if len(founds) > 0:
        found = founds[0]
        found = found.replace('</font>', '')
        return found


if __name__ == '__main__':
    getData()
