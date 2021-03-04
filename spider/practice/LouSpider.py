# coding: utf-8
# Author：chyh
# Date ：2021/2/4 11:28

from bs4 import BeautifulSoup
import re
import urllib
from urllib import request, parse
from myTools import mySql
import os
import time

baseUrl = "http://www.xiaohongloubb.com/"
provinceId = '36'
dataList = []
markdownFile = "info_" + provinceId + ".md"


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
        print(e)
    except ConnectionResetError as e:
        print(e)
    except UnboundLocalError as e:
        print(e)
    return response


def getData():
    # print("开始获取页面链接")
    while True:
        result = getPostContents()
        if not result:
            time.sleep(5)
        else:
            print("搞定")


def getPageLinks():
    url = baseUrl + "forum.php?mod=forumdisplay&fid=" + provinceId
    html = askUrl(url)
    soup = BeautifulSoup(html, "html.parser")
    findPageCount = re.compile(r'<span title="共(.*?)页"')
    pageCount = re.findall(findPageCount, str(soup))
    pageCount = int(pageCount[0].strip())
    pageLinks = []
    for i in range(0, pageCount):
        link = baseUrl + "forum.php?mod=forumdisplay&fid=" + provinceId + "&page=" + str(i + 1)
        print(link)
        pageLinks.append(link)
    getPostLinks(pageLinks)


def getPostLinks(pageLinks):
    postIds = []
    print("开始打印postId")
    for pageLink in pageLinks:
        html = askUrl(pageLink)
        soup = BeautifulSoup(html, "html.parser")
        findPostId = re.compile(r'<tbody id="normalthread_(.*)">')
        postId = re.findall(findPostId, str(soup))
        postIds.extend(postId)
        print(pageLink)
        print(postId)
        insertPostIdsToDatabase(postId)
    return postIds


def insertPostIdsToDatabase(postIds):
    baseSql = "insert into POST_ID(post_id,is_download,province_id) values('"
    conn = mySql.MyPythonSql()
    for postId in postIds:
        sql = baseSql + postId + "', '0', '" + provinceId + "')"
        conn.insert(sql=sql)
    conn.close()


def getPostContents():
    conn = mySql.MyPythonSql()
    postIds = conn.query("select post_id from POST_ID where is_download = '0'")
    conn.close()
    basePostUrl = "http://www.xiaohonglouss.com/forum.php?mod=viewthread&tid="
    for postId in postIds:
        url = basePostUrl + postId[0]
        try:
            html = askUrl(url)
        except urllib.error.URLError as e:
            print(e)
            return False
        except ConnectionResetError as e:
            print(e)
            return False
        soup = BeautifulSoup(html, "html.parser")
        content = [postId[0], soup]
        processPostContents(content)
    return True


def processPostContents(content):
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
    print("获取帖子" + postId)
    title = getSpecifiedPattern(soup, r'<span id="thread_subject">(.*?)</span>')
    date = getSpecifiedPattern(soup, r'【验证时间】：(.*)<br/>')
    location = getSpecifiedPattern(soup, r'【验证地点】：(.*)<br/>')
    env = getSpecifiedPattern(soup, r'【环境设备】：(.*)<br/>')
    price = getSpecifiedPattern(soup, r'【价格一览】：(.*)<br/>')
    keyPoint = getSpecifiedPattern(soup, r'【重点推荐】：(.*)<br/>')
    detail = getSpecifiedPattern(soup, r'【验证细节】：(.*)<br/>')
    downloadImg(postId, soup)
    # print(postId)
    # print(title)
    # print(date)
    # print(location)
    # print(env)
    # print(price)
    # print(keyPoint)
    # print(detail)
    print("=============================")
    sql = "insert into POST_CONTENT(post_id,title,date,location,env,price,keypoint,detail) values('" \
          + postId + "','" \
          + title + "','" \
          + date + "','" \
          + location + "','" \
          + env + "','" \
          + price + "','" \
          + keyPoint + "','" \
          + detail + "')"
    conn = mySql.MyPythonSql()
    conn.insert(sql)
    conn.update("update POST_ID set is_download = '1' where post_id = '" + postId + "'")
    conn.close()


def getSpecifiedPattern(soup, example):
    pattern = re.compile(example)
    founds = re.findall(pattern, str(soup))
    found = ''
    if len(founds) > 0:
        found = founds[0]
        found = re.sub(r"<font.*>", '', found)
    return found


def downloadImg(postId, soup):
    imgList = []
    for item in soup.find_all("img", class_="zoom"):
        file = item['file']
        imgLink = baseUrl + file
        imgList.append(imgLink)
    for i in range(1, len(imgList) + 1):
        imgLink = imgList[i - 1]
        filePath = "./imgs/" + postId + "/"
        if not os.path.exists(filePath):
            os.mkdir(filePath)
        try:
            request.urlretrieve(imgLink, filePath + postId + "_" + str(i) + ".jpg")
        except urllib.error.URLError as e:
            print(e)
        except ConnectionResetError as e:
            print(e)


def makeMarkdown():
    conn = mySql.MyPythonSql()
    postContents = conn.query("select post_id,title,date,location,env,price,keypoint,detail from POST_CONTENT")
    conn.close()
    if os.path.exists(markdownFile):
        os.remove(markdownFile)
    fo = open(markdownFile, 'w')
    for postContent in postContents:
        writeMarkdown(fo, postContent)
    fo.close()


def writeMarkdown(fo, postContent):
    print(postContent[0])
    content = "## " + "".join(postContent[0].split()) + "  --  " + "".join(postContent[1].split()) + "\n" \
              + "**日期** : " + "".join(postContent[2].split()) + "\n" \
              + "**地点** : " + "".join(postContent[3].split()) + "\n" \
              + "**环境** : " + "".join(postContent[4].split()) + "\n" \
              + "**价格** : " + "".join(postContent[5].split()) + "\n" \
              + "**关键** : " + "".join(postContent[6].split()) + "\n" \
              + "**细节** : " + "".join(postContent[7].split()) + "\n"
    imgList = getImgList(postContent[0])
    for imgPath in imgList:
        content += "![](" + imgPath + ")\n"
    content += "\n\n\n"
    fo.write(content)


def getImgList(postId):
    path = "./imgs/" + postId + "/"
    if os.path.exists(path):
        pathList = []
        relativePath = os.listdir(path)
        for fileName in relativePath:
            pathList.append(path + fileName)
        return pathList
    else:
        return []


if __name__ == '__main__':
    getPageLinks()
    # getData()
    # makeMarkdown()
