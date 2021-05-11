# Coding : utf-8
# Author : chyh
# Date   : 2021/3/29 21:58

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String,Date

Base = declarative_base()


class film_bean(Base):
    # 默认的表名
    __tablename__ = 'ONLINE_LINKS'

    title = Column(String(500))

    url = Column(String(500), primary_key=True)

    post_date = Column(Date())

    reply_count = Column(Integer())

    '''
    0 没看过的
    1 正在看的
    2 看完了的
    '''
    status = Column(Integer())

    def __init__(self, title, url, post_date, reply_count):
        self.title = title
        self.url = url
        self.post_date = post_date
        self.reply_count = reply_count
        self.status = 0
