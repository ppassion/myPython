# Coding : utf-8
# Author : chyh
# Date   : 2021/3/8 20:42

import logging


def get_logger():
    """
    创建日志单例
    """
    global logger
    formatter = logging.Formatter("%(asctime)s %(name)s:%(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S")
    logger = logging.getLogger("monitor")
    logger.setLevel(logging.INFO)
    handler_stream = logging.StreamHandler()
    handler_stream.setLevel(logging.INFO)
    handler_stream.setFormatter(formatter)
    handler_error = logging.FileHandler(filename="error.log", encoding="utf-8")
    handler_error.setLevel(logging.ERROR)
    handler_error.setFormatter(formatter)
    logger.addHandler(handler_stream)
    logger.addHandler(handler_error)
    return logger


logger = get_logger()
