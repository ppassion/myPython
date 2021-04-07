# Coding : utf-8
# Author : chyh
# Date   : 2021/4/5 20:54

import threading
from proxySpider.i_proxy_spider import i_proxy_spider


class get_proxy_thread(threading.Thread, i_proxy_spider):
    def do_resolve(self, res) -> list:
        pass

    def get_page_urls(self) -> str:
        pass

    def __init__(self, proxy_name):
        threading.Thread.__init__(self)
        self.proxy_name = "Thread-" + proxy_name

    def run(self) -> None:
        self.crawl()
