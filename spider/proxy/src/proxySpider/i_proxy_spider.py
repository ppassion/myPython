# Coding : utf-8
# Author : chyh
# Date   : 2021/3/10 23:44

from spider.proxy.src.log.logger import logger
from common.setting import header

import aiohttp
import asyncio


class i_proxy_spider(object):

    def __init__(self):
        print(1111)

    async def crawl(self):
        logger.info('==' + self._name + "==开始爬取")
        resolve_list = []
        try:
            for url in self.get_page_urls():
                async with aiohttp.ClientSession() as session:
                    async with session.get(url=url, headers=header) as res:
                        resolve = self.do_resolve(await res.text())
                        resolve_list.extend(resolve)
                        await asyncio.sleep(self.get_interval())
        except Exception as e:
            logger.error('==' + self._name + "==爬取失败")
            logger.error(e)
        return resolve_list

    # 返回默认爬取的页面列表
    def get_page_urls(self) -> str:
        raise NotImplementedError

    def get_encoding(self):
        return 'utf-8'
        raise NotImplementedError

    def do_resolve(self, res) -> list:
        raise NotImplementedError

    def get_interval(self) -> int:
        return 5
        raise NotImplementedError
