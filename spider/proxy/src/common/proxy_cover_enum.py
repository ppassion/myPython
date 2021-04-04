# Coding : utf-8
# Author : chyh
# Date   : 2021/4/2 18:33

from enum import Enum, unique


@unique
class proxy_cover_enum(Enum):

    UNKNOWN = '未知'

    # 透明
    TRANSPARENT = '透明'

    # 匿名
    NORMAL_COVER = '匿名'

    # 高匿
    HIGH_COVER = '高匿'
