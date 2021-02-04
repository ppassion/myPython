# coding: utf-8
# Author：chyh
# Date ：2021/2/4 11:28

import urllib
from urllib import request, parse
import requests

baidu = "http://www.baidu.com"
httpbin = "http://httpbin.org"


def httpGet():
    response = request.urlopen(baidu)
    print(response.read().decode('utf-8'))
    # print(response.status)
    # print(response.getheader("Server"))
    # print(response.)


def httpPost():
    data = bytes(parse.urlencode({"hello": "world"}), encoding="utf-8")
    try:
        response = request.urlopen(httpbin + "/post", data=data, timeout=0.01)
        print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print("timeout")


def customize():
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/88.0.4324.104 Safari/537.36 "
        }
        data = bytes(parse.urlencode({"hello": "world"}), encoding="utf-8")
        req = request.Request(httpbin + "/post", data=data, headers=headers, method="POST")
        response = request.urlopen(req)
        print(response.read().decode('utf-8'))
        # print(response.getheader("User-Agent"))
    except urllib.error.URLError as e:
        print("timeout")


if __name__ == '__main__':
    # httpGet()
    # httpPost()
    customize()
