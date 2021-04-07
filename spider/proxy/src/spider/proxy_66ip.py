# Coding : utf-8
# Author : chyh
# Date   : 2021/3/27 22:01
from typing import Iterable

from spider.proxy.src.proxySpider.i_proxy_spider import i_proxy_spider
from common.setting import available_days

from bs4 import BeautifulSoup
import asyncio
import math


class proxy_66ip(i_proxy_spider):

    def __init__(self):
        self._name = '66ip'

    '''
    ===链接样式===

    http://www.66ip.cn/1.html
    编号从1到2000+，大编号对应的IP失效概率比较高

    2小时更新一次，每次更新一条，每页10条
    保存${setting.available_days}(默认30)天内的，共360条，即取前36页
    '''
    num_per_day = 12
    num_per_page = 10

    def get_page_urls(self) -> str:
        urls = []
        max_page_num = math.ceil(available_days * self.num_per_day / self.num_per_page)
        for i in range(1, max_page_num + 1):
            url = "http://www.66ip.cn/" + str(i) + ".html"
            urls.append(url)
        return urls

    def do_resolve(self, res) -> list:
        resolve_result = []
        soup = BeautifulSoup(res, 'lxml')
        tr_list = soup.find('table', attrs={'width': '100%', 'bordercolor': '#6699ff'}).find_all('tr')
        for tr in tr_list:
            tds = tr.find_all('td')
            print(tds)
        print(tr_list)
