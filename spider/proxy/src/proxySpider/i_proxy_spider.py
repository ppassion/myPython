# Coding : utf-8
# Author : chyh
# Date   : 2021/3/10 23:44

from spider.proxy.src.log.logger import logger
from typing import Iterable
from spider.proxy.src.setting import header

import aiohttp
import asyncio


class i_proxy_spider(object):

    def __init__(self, name='unknown'):
        self._name = name
        self._urls = self.get_urls()

    def crawl(self):
        logger.info(self._name + "开始爬取")
        resolve_list = []
        for url in self._urls:
            try:
                for page in self.get_page_range():
                    async with aiohttp.ClientSession() as session:
                        async with session.get(self.get_page_urls(baseUrl=url, page=page), headers=header) as res:
                            res.charset = self.get_encoding()
                            resolve = self.do_resolve(await res.text())
                            resolve_list.extend(resolve)
                            await asyncio.sleep(self.get_interval())
            except Exception as e:
                logger.error(self._name + "爬取失败")
                logger.error(e)
        return resolve_list

    def get_urls(self) -> list[str]:
        raise NotImplementedError

    # 返回默认爬取的页面列表
    def get_page_range(self) -> Iterable:
        return range(1, 2)
        raise NotImplementedError

    def get_page_urls(self, baseUrl, page) -> str:
        return baseUrl + page
        raise NotImplementedError

    def get_encoding(self):
        return 'utf-8'
        raise NotImplementedError

    def do_resolve(self,res) -> list:
        raise NotImplementedError

    def get_interval(self) -> int:
        return 5
        raise NotImplementedError
