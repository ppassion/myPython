# Coding : utf-8
# Author : chyh
# Date   : 2021/3/10 23:44

from spider.proxy.src.log.logger import logger
from common.setting import header

import asyncio
from urllib import request, parse
from bs4 import BeautifulSoup
import time


class i_proxy_spider(object):

    def askUrl(self, url):
        data = bytes(parse.urlencode({"hello": "world"}), encoding="utf-8")
        req = request.Request(url, data=data, headers=header, method="GET")
        soup = None
        somethingHappened = False
        # noinspection PyBroadException
        try:
            response = request.urlopen(req)
            # soup = BeautifulSoup(response, "html.parser")
        except BaseException:
            somethingHappened = True
        except OSError:
            somethingHappened = True
        except ConnectionResetError:
            somethingHappened = True
        return response, somethingHappened

    def crawl(self):
        logger.info('==' + self._name + "==开始爬取")
        resolve_list = []
        try:
            for url in self.get_page_urls():
                print(url)
                while True:
                    response, somethingHappened = self.askUrl(url)
                    if somethingHappened:
                        time.sleep(5)
                    else:
                        break
                resolve = self.do_resolve(response)
                resolve_list.extend(resolve)
                time.sleep(self.get_interval())
        except Exception as e:
            logger.error('==' + self._name + "==爬取失败")
            logger.error(e)
        return resolve_list

    # 返回默认爬取的页面列表
    def get_page_urls(self) -> str:
        raise NotImplementedError

    def get_encoding(self):
        raise NotImplementedError
        return 'utf-8'

    def do_resolve(self, res) -> list:
        raise NotImplementedError

    def get_interval(self) -> int:
        raise NotImplementedError
        return 5
