# Coding : utf-8
# Author : chyh
# Date   : 2021/4/5 20:13

from datetime import datetime
from common.setting import available_days

"""
True表示是有效期内的
False表示有效期外
"""


def check_update_time(update_time: datetime) -> bool:
    now = datetime.now()
    seconds_diff = (now - update_time).seconds
    # 更新时间有效期外的不再使用
    if seconds_diff > available_days * 24 * 60 * 60:
        return False
    else:
        return True
