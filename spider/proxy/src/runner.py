# Coding : utf-8
# Author : chyh
# Date   : 2021/3/8 20:37

from spider.proxy.src.log.logger import logger
from spider.proxy.src.db.DbOpt import dbOpt


def run():
    logger.warning('初始化sqlite数据库...')
    logger.info('初始化sqlite数据库...')
    logger.error('初始化sqlite数据库...')
    # dbOpt.create_table()
    # scheduler = BackgroundScheduler()
    # scheduler.add_job(crawl, 'interval', seconds=SPIDER['crawl_interval'])
    # scheduler.add_job(validator.run, 'interval', seconds=VALIDATOR['validate_interval'])
    # scheduler.add_job(anonymity_validator.run, 'interval', seconds=ANONYMITY_VALIDATOR['interval'])
    # scheduler.add_job(expiration_validator.run, 'interval', seconds=EXPIRATION_VALIDATOR['interval'])
    # scheduler.start()
    # app.run(host=WEB_SERVER['host'], port=WEB_SERVER['port'])
