# Coding : utf-8
# Author : chyh
# Date   : 2021/3/29 21:58

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class proxy_bean(Base):
    __tablename__ = 'proxy'
    ip = Column(String(20), primary_key=True)
    port = Column(String(5))

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
