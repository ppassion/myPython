# Coding : utf-8
# Author : chyh
# Date   : 2021/3/27 22:01


from bean.proxy_bean import proxy_bean
from db.database_opt import database_opt
from proxySpider.i_proxy_spider import i_proxy_spider
from common.type_formatter import type_formatter
from common.setting import available_days

from bs4 import BeautifulSoup
from datetime import datetime
import math


class proxy_kuaidaili(i_proxy_spider):

    def __init__(self):
        self._name = '快代理'

    '''
    ===链接样式===
    
    高匿代理
    https://www.kuaidaili.com/free/inha/1/
    普通代理
    https://www.kuaidaili.com/free/intr/1/
    编号从1到3000+，大编号对应的IP失效概率比较高，需要校验
    
    每小时更新一次，每次透明和高匿的各更新一条，每页15条
    保存${setting.available_days}(默认7)天内的，共168条，即取前12页
    '''

    def get_page_urls(self) -> str:
        urls = []
        max_page_num = math.ceil(available_days * 24 / 15)
        for i in range(1, max_page_num + 1):
            url_inha = "https://www.kuaidaili.com/free/inha/" + str(i)
            url_intr = "https://www.kuaidaili.com/free/inha/" + str(i)
            urls.append(url_inha)
            urls.append(url_intr)
        return urls

    def do_resolve(self, res) -> list:
        resolve_result = []
        soup = BeautifulSoup(res, 'lxml')
        trs = soup.find('table').find('tbody').find_all('tr')
        for tr in trs:
            tds = tr.find_all('td')
            ip = tds[0].text
            port = tds[1].text
            proxy_cover = type_formatter.proxy_cover_formatter(tds[2].text)
            proxy_type = type_formatter.proxy_type_formatter(tds[3].text)
            update_time = tds[6].text
            if self.check_update_time(update_time):
                new_proxy = proxy_bean(ip, port, None, self._name, proxy_type, proxy_cover)
                database_opt.add_proxy(new_proxy)
                resolve_result.append(new_proxy)
            else:
                break
        return resolve_result

    '''
    True表示是7天内的
    False表示7天外
    '''
    @staticmethod
    def check_update_time(update_time) -> bool:
        now = datetime.now()
        update_time = datetime.strptime(update_time, '%Y-%m-%d %H:%M:%S')
        seconds_diff = (now - update_time).seconds
        # 更新时间7天前的不再使用
        if seconds_diff > available_days * 24 * 60 * 60:
            return False
        else:
            return True


if __name__ == '__main__':
    proxy_kuaidaili().check_update_time('2021-04-04 10:31:01')
