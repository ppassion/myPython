# coding : utf-8
# Author : chyh
# Date   : 2021/2/5 22:38

from bs4 import BeautifulSoup
from urllib import request, parse
import re

baidu = "http://www.baidu.com"


def beautifulsoup():
    response = request.urlopen(baidu)
    html = response.read()
    bs = BeautifulSoup(html, "html.parser")
    print(bs.a)


def findAll():
    response = request.urlopen(baidu)
    html = response.read()
    bs = BeautifulSoup(html, "html.parser")
    # a_list = bs.findAll("a")
    a_list = bs.findAll(re.compile("head"))
    print(a_list)


if __name__ == '__main__':
    findAll()
