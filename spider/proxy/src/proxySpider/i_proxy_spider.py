# Coding : utf-8
# Author : chyh
# Date   : 2021/3/10 23:44

from spider.proxy.src.log.logger import logger


class i_proxy_spider(object):

    def __init__(self, name='unknown'):
        self._name = name
        self._urls = self.get_urls()

    def get_urls(self) -> list[str]:
        raise NotImplementedError

    def crawl(self):
        logger.info(self._name + "开始爬取")
        for url in self._urls:
            print(11)
