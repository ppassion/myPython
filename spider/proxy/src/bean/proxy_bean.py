# Coding : utf-8
# Author : chyh
# Date   : 2021/3/29 21:58

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class proxy_bean(Base):

    # 默认的表名
    __tablename__ = 'proxy'

    ip = Column(String(20), primary_key=True)
    port = Column(String(5))

    # 来源网站
    source = Column(String(50))

    # 代理实际提供者
    supplier = Column(String(50))

    # 代理类型
    proxy_type = Column(Integer())

    # 代理匿名类型
    proxy_cover = Column(String(50))

    # 有效性检验的次数
    # check_count = Column(String(50))
    # region = Column(String(50))

    def __init__(self, ip, port, source, supplier, proxy_type, proxy_cover):
        self.ip = ip
        self.port = port
        self.source = source
        self.supplier = supplier
        self.proxy_type = proxy_type
        self.proxy_cover = proxy_cover
