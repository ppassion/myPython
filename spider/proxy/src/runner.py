# Coding : utf-8
# Author : chyh
# Date   : 2021/3/8 20:37

from log.logger import logger
from db.database_opt import database_opt
from proxySpider.i_proxy_spider import i_proxy_spider
from spider.proxy_kuaidaili import proxy_kuaidaili

import asyncio


def crawl():
    kuaidaili = proxy_kuaidaili()
    kuaidaili.crawl()
    # tasks = []
    # crawler = proxy_kuaidaili().crawl()
    # tasks.append(crawler)
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # results = loop.run_until_complete(asyncio.gather(*tasks))
    # loop.close()
    # for external_proxy in external_proxies:
    # tasks.append(spider_collection[spider_name].crawl())
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # results = loop.run_until_complete(asyncio.gather(*tasks))
    # loop.close()
    # for proxies_list in results:
    #     proxies.extend(proxies_list)
    # # proxies = loop.run_until_complete(asyncio.gather(*tasks))
    # # 持久化
    # save(proxies)


def run():
    logger.info("初始化数据库，调起定时任务")
    database_opt.create_table()
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(f, 'interval', seconds=3)
    # scheduler.start()
    # scheduler.add_job(crawl, 'interval', seconds=SPIDER['crawl_interval'])
    # scheduler.add_job(validator.run, 'interval', seconds=VALIDATOR['validate_interval'])
    # scheduler.add_job(anonymity_validator.run, 'interval', seconds=ANONYMITY_VALIDATOR['interval'])
    # scheduler.add_job(expiration_validator.run, 'interval', seconds=EXPIRATION_VALIDATOR['interval'])
    # scheduler.start()
    # app.run(host=WEB_SERVER['host'], port=WEB_SERVER['port'])


if __name__ == '__main__':
    # run()
    crawl()
