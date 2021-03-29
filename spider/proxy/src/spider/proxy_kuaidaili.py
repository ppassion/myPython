# Coding : utf-8
# Author : chyh
# Date   : 2021/3/27 22:01
from typing import Iterable

from bean.proxy_bean import proxy_bean
from db.database_opt import database_opt
from proxySpider.i_proxy_spider import i_proxy_spider
from bs4 import BeautifulSoup


class proxy_kuaidaili(i_proxy_spider):

    def __init__(self):
        self._name = '==快代理=='

    '''
    ===链接样式===
    
    高匿代理
    https://www.kuaidaili.com/free/inha/1/
    普通代理
    https://www.kuaidaili.com/free/intr/1/
    编号从1到3000+，大编号对应的IP失效概率比较高，需要校验
    '''

    def get_page_urls(self) -> str:
        urls = []
        for i in range(1, 2):
            url = "https://www.kuaidaili.com/free/inha/" + str(i)
            urls.append(url)
        return urls

    def do_resolve(self, res) -> list:
        resolve_result = []
        soup = BeautifulSoup(res, 'lxml')
        trs = soup.find('table').find('tbody').find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            ip = tds[0].text
            port = tds[1].text
            anonymity = tds[2].text
            proxy_type = tds[3].text
            updateTime = tds[6].text
            new_proxy = proxy_bean(ip,port)
            database_opt.add_proxy(new_proxy)
