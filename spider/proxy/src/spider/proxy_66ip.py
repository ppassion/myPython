# Coding : utf-8
# Author : chyh
# Date   : 2021/3/27 22:01
from typing import Iterable

from spider.proxy.src.proxySpider.i_proxy_spider import i_proxy_spider
from bs4 import BeautifulSoup

import asyncio

class proxy_66ip(i_proxy_spider):

    def get_page_urls(self) -> str:
        urls = []
        for i in range(1, 35):
            url = "http://www.66ip.cn/areaindex_" + str(i) + "/1.html"
            urls.append(url)
        return urls

    def do_resolve(self, res) -> list:
        resolve_result = []
        soup = BeautifulSoup(res,'lxml')
        tr_list = soup.find('table', attrs={'width': '100%', 'bordercolor': '#6699ff'}).find_all('tr')
        for tr in tr_list:
            tds = tr.find_all('td')
            print(tds)
        print(tr_list)

    def f(self):
        print(1111)


if __name__ == '__main__':
    aa = proxy_66ip()
    # aa.do_resolve(aa.crawl())
    tasks = [aa.crawl()]
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    results = loop.run_until_complete(asyncio.gather(*tasks))
    loop.close()