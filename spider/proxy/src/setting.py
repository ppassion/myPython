# Coding : utf-8
# Author : chyh
# Date   : 2021/3/10 0:46


# 数据库配置
database_info = {
    'db_name': 'proxy.db',
    'ddl': '''
            create table if not exists proxy(
            url varchar(36) not null,
            source varchar(16), 
            supplier varchar(32),
            proxy_type tinyint(3), 
            proxy_cover tinyint(3), 
            check_count int(10), 
            region varchar(36), 
            last_check_time text,
            create_time text default (datetime(CURRENT_TIMESTAMP,'localtime')),
            reliability integer not null default 0 check(reliability >= 0) check(reliability <= 15),
            PRIMARY KEY ("url")
            )
            '''
}

log_color = {
    'yellow': '\033[1;33m',
    'red': '\033[1;31m',
    'white': '\033[1;37m'
}