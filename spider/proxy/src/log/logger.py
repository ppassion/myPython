# Coding : utf-8
# Author : chyh
# Date   : 2021/3/8 20:42

import logging
from spider.proxy.src.setting import log_color


class myLogger(object):
    myLogger = None
    stream_handler = logging.StreamHandler()
    logging.basicConfig(level=logging.DEBUG)

    def __init__(self):
        self.myLogger = logging.getLogger("monitor")
        self.myLogger.propagate = 0

    def warning(self, message):
        self.fontColor(log_color['yellow'], logging.WARNING)
        self.myLogger.warning(message)

    def info(self, message):
        self.fontColor(log_color['white'], logging.INFO)
        self.myLogger.info(message)

    def error(self, message):
        self.fontColor(log_color['red'], logging.ERROR)
        self.myLogger.error(message)

    def fontColor(self, color, level):
        # 不同的日志输出不同的颜色
        formatter = logging.Formatter(color + '[%(asctime)s] - [%(levelname)s] - %(message)s')
        self.stream_handler.setLevel(level)
        self.stream_handler.setFormatter(formatter)
        self.myLogger.addHandler(self.stream_handler)


logger = myLogger()
