# Coding : utf-8
# Author : chyh
# Date   : 2021/3/29 21:58

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class proxy_bean(Base):
    '''
                create table if not exists proxy(
                ip varchar(20) not null,
                port varchar(5) not null,
                source varchar(50),
                supplier varchar(32),
                proxy_type tinyint(3),
                proxy_cover tinyint(3),
                check_count int(10),
                region varchar(36),
                last_check_time text,
                create_time text default (datetime(CURRENT_TIMESTAMP,'localtime')),
                reliability integer not null default 0 check(reliability >= 0) check(reliability <= 15),
                PRIMARY KEY ("ip","port")
                )

                '''
    __tablename__ = 'proxy'
    ip = Column(String(20), primary_key=True)
    port = Column(String(5))

    # 来源网站
    source = Column(String(50))

    # 代理实际提供者
    supplier = Column(String(50))

    # 代理类型
    proxy_type = Column(Integer())
    proxy_cover = Column(String(50))
    check_count = Column(String(50))
    region = Column(String(50))

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
