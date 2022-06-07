# -*- coding: utf-8 -*-
# @Time : 2022/6/7 9:20 下午
# @Author : chenxiangan
# @File : run2.py
# @Software: PyCharm
from twisted.internet import reactor,defer
from scrapy.crawler import  CrawlerRunner
from scrapy.utils.log import configure_logging
import time
import logging
from scrapy.utils.project import get_project_settings

#在控制台输出日志
configure_logging()
#CrawlerRunner获取settings.py里的设置信息
runner = CrawlerRunner(get_project_settings())
@defer.inlineCallbacks
def crawl():
    while True:
        logging.info("start crawl")
        yield runner.crawl('baidu_spider')
        #一分钟一次
        time.sleep(60)
    reactor.stop()

if __name__ == '__main__':
    crawl()
    reactor.run()