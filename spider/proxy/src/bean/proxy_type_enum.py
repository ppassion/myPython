# Coding : utf-8
# Author : chyh
# Date   : 2021/4/2 18:33

from enum import Enum, unique


@unique
class proxy_type_enum(Enum):
    UNKNOWN = 0
    HTTP = 1
    HTTPS = 2
    HTTP_AND_HTTPS = 3
