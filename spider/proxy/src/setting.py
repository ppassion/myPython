# Coding : utf-8
# Author : chyh
# Date   : 2021/3/10 0:46


# 数据库配置
database_info = {
    'db_name': 'proxy.db',
    'ddl': '''
            create table if not exists proxy(
            ip varchar(20) not null,
            port varchar(5) not null,
            source varchar(16), 
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
}

log_color = {
    'yellow': '\033[1;33m',
    'red': '\033[1;31m',
    'white': '\033[1;37m'
}

header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/88.0.4324.104 Safari/537.36 "
    }

external_proxies = {
    '66Ip',
    'QuanWangIp',
    'XiciIp',
    'KuaiDaiLiIp',
    'YunDaiLiIp',
    'IpHaiIp',
    'MianFeiDaiLiIp'
}