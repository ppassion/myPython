# coding: utf-8
# Author：chyh
# Date ：2021/2/4 11:28


from bs4 import BeautifulSoup
import re
from urllib import request, parse
from myTools import mySql
import os
import time
import shutil
import socket
import yaml

configFile = open("urlInfo.yml", 'r', encoding='utf-8')
config = configFile.read()
configMap = yaml.load(config, Loader=yaml.FullLoader)
provinceId = '36'
dataList = []
markdownFile = "info_" + provinceId + ".md"
somethingHappened = False
socket.setdefaulttimeout(10)


def askUrl(url):
    global somethingHappened
    header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.104 Safari/537.36 "
    }
    data = bytes(parse.urlencode({"hello": "world"}), encoding="utf-8")
    req = request.Request(url, data=data, headers=header, method="GET")
    soup = None
    try:
        response = request.urlopen(req)
        soup = BeautifulSoup(response, "html.parser")
    except BaseException as e:
        # print(url)
        # print(e)
        somethingHappened = True
    except OSError as e:
        # print(url)
        # print(e)
        somethingHappened = True
    except ConnectionResetError as e:
        # print(url)
        # print(e)
        somethingHappened = True
    except socket.timeout as e:
        # print(url)
        # print(e)
        somethingHappened = True
    return soup


def retrieveUrl(imgLink, filePath):
    global somethingHappened
    try:
        request.urlretrieve(imgLink, filePath)
    except BaseException as e:
        # print(imgLink)
        # print(e)
        somethingHappened = True
    except OSError as e:
        # print(imgLink)
        # print(e)
        somethingHappened = True
    except ConnectionResetError as e:
        # print(imgLink)
        # print(e)
        somethingHappened = True
    except socket.timeout as e:
        # print(imgLink)
        # print(e)
        somethingHappened = True


def getData():
    getPostContents()


def getPageLinks():
    url = configMap["pageBaseUrl"] + provinceId
    soup = askUrl(url)
    findPageCount = re.compile(r'<span title="共(.*?)页"')
    pageCount = re.findall(findPageCount, str(soup))
    pageCount = int(pageCount[0].strip())
    print("共有" + str(pageCount) + "页")
    for i in range(0, pageCount):
        pageLink = configMap["pageBaseUrl"] + provinceId + "&page=" + str(i + 1)
        print(pageLink)
        getPostLinks(pageLink)


def getPostLinks(pageLink):
    global somethingHappened
    postIds = []
    while True:
        somethingHappened = False
        soup = askUrl(pageLink)
        if somethingHappened:
            # print("出事了,等5秒")
            time.sleep(5)
        else:
            break
    findPostId = re.compile(r'<tbody id="normalthread_(.*)">')
    postId = re.findall(findPostId, str(soup))
    postIds.extend(postId)
    insertPostIdsToDatabase(postId)


def insertPostIdsToDatabase(postIds):
    baseSql = "insert into POST_ID(post_id,is_download,province) values('"
    conn = mySql.MyPythonSql()
    for postId in postIds:
        sql = baseSql + postId + "', '0', '" + provinceId + "')"
        conn.insert(sql=sql)
    conn.close()


def getPostContents():
    global somethingHappened
    conn = mySql.MyPythonSql()
    postIds = conn.query("select post_id from POST_ID where is_download = '0' and province = '" + provinceId + "'")
    # postIds = conn.query("select post_id from POST_ID where post_id = '3865'")
    conn.close()
    print("共有" + str(len(postIds)) + "个帖子需要解析")
    size = len(postIds)
    for i in range(0, size):
        startTime = time.time()
        postId = postIds[i][0]
        url = configMap["postBaseUrl"] + postId
        while True:
            somethingHappened = False
            soup = askUrl(url)
            if somethingHappened:
                # print("出事了,等5秒")
                time.sleep(5)
            else:
                break
        content = [postId, soup]
        processPostContents(content)
        endTime = time.time()
        print(str(i + 1) + "/" + str(size) + "   " + postId +
              " 耗时" + str(int(endTime - startTime)) + "秒")


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
    # print("获取帖子具体信息" + postId)
    title = getSpecifiedPattern(soup, r'<span id="thread_subject">(.*?)</span>')
    date = getSpecifiedPattern(soup, r'【验证时间】：(.*)<br/>')
    location = getSpecifiedPattern(soup, r'【验证地点】：(.*)<br/>')
    env = getSpecifiedPattern(soup, r'【环境设备】：(.*)<br/>')
    price = getSpecifiedPattern(soup, r'【价格一览】：(.*)<br/>')
    keyPoint = getSpecifiedPattern(soup, r'【重点推荐】：(.*)<br/>')
    detail = getSpecifiedPattern(soup, r'【验证细节】：(.*)<br/>')
    downloadImg(postId, soup)
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
    global somethingHappened
    imgList = []
    for item in soup.find_all("img", class_="zoom"):
        if item.attrs.__contains__('file'):
            file = item['file']
            imgLink = configMap["baseUrl"] + file
            imgList.append(imgLink)
    filePath = "./imgs/" + postId + "/"
    if os.path.exists(filePath):
        shutil.rmtree(filePath)
    os.mkdir(filePath)
    for i in range(1, len(imgList) + 1):
        imgLink = imgList[i - 1]
        while True:
            somethingHappened = False
            retrieveUrl(imgLink, filePath + postId + "_" + str(i) + ".jpg")
            if somethingHappened:
                # print("出事了,等5秒")
                time.sleep(5)
            else:
                break


def makeMarkdown():
    conn = mySql.MyPythonSql()
    postContents = conn.query(
        "select post_id,title,date,location,env,price,keypoint,detail from POST_CONTENT "
        "where province = '" + provinceId + "'")
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
    print("开始时间 " + time.strftime("%H:%M:%S"))
    # getPageLinks()
    getData()
    # makeMarkdown()
    print("结束时间 " + time.strftime("%H:%M:%S"))
