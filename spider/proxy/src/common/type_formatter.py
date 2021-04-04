# Coding : utf-8
# Author : chyh
# Date   : 2021/4/4 10:44

from common.proxy_type_enum import proxy_type_enum
from common.proxy_cover_enum import proxy_cover_enum


class type_formatter(object):
    @staticmethod
    def proxy_type_formatter(proxy_type: str) -> str:
        if proxy_type == 'HTTP':
            formatted_proxy_type = proxy_type_enum.HTTP.value
        elif proxy_type == 'HTTPS':
            formatted_proxy_type = proxy_type_enum.HTTPS.value
        else:
            formatted_proxy_type = proxy_type_enum.UNKNOWN.value
        return formatted_proxy_type

    @staticmethod
    def proxy_cover_formatter(proxy_type: str) -> str:
        if proxy_type == 'HTTP':
            formatted_proxy_cover = proxy_cover_enum.TRANSPARENT.value
        elif proxy_type == '高匿名':
            formatted_proxy_cover = proxy_cover_enum.HIGH_COVER.value
        else:
            formatted_proxy_cover = proxy_cover_enum.UNKNOWN.value
        return formatted_proxy_cover


type_formatter = type_formatter()
