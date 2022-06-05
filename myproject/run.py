# -*- coding: utf-8 -*-
# @Time : 2022/6/5 12:54 下午
# @Author : chenxiangan
# @File : run.py.py
# @Software: PyCharm
import time

from scrapy import signals
from scrapy.crawler import CrawlerProcess, Crawler

from myproject import settings as scrapy_settings


class MySpider():
    def __init__(self):
        self.settings = {
            'BOT_NAME': scrapy_settings.BOT_NAME,
            'SPIDER_MODULES': scrapy_settings.SPIDER_MODULES,
            'NEWSPIDER_MODULE': scrapy_settings.NEWSPIDER_MODULE,
            'ROBOTSTXT_OBEY': scrapy_settings.ROBOTSTXT_OBEY,
            'DOWNLOADER_MIDDLEWARES': scrapy_settings.DOWNLOADER_MIDDLEWARES,
            'SPIDER_MIDDLEWARES': scrapy_settings.SPIDER_MIDDLEWARES,
            'ITEM_PIPELINES': scrapy_settings.ITEM_PIPELINES,
            'DEFAULT_REQUEST_HEADERS': scrapy_settings.DEFAULT_REQUEST_HEADERS,
            'EXTENSIONS': scrapy_settings.EXTENSIONS,
            'DOWNLOAD_DELAY': scrapy_settings.DOWNLOAD_DELAY,
            'DOWNLOAD_TIMEOUT': 30,
            'LOG_LEVEL': scrapy_settings.LOG_LEVEL,
            'COOKIES_ENABLED': scrapy_settings.COOKIES_ENABLED,
            'CONCURRENT_REQUESTS': scrapy_settings.CONCURRENT_REQUESTS,
        }

    def crawler_signals(self, crawler):
        signals_dict = {
            self.spider_opened: signals.spider_opened,
            self.spider_closed: signals.spider_closed,
            self.spider_error: signals.spider_error,
            self.request_reached_downloader: signals.request_reached_downloader,
        }
        for func, signals_func in signals_dict.items():
            crawler.signals.connect(func, signal=signals_func)
        return crawler

    def spider_opened(self, spider):
        spider.crawler.stats.set_value("spider_start_time", int(time.time()))

    def spider_closed(self, spider):
        print("spider_closed")

    def spider_error(self, spider):
        print("spider_error")

    def request_reached_downloader(self, spider):
        """
        每当请求到达下载器时，它都会发出 request_reached_downloader 信号。下载后，它发出 response_downloaded 信号
        :param spider:
        :return:
        """
        print("request_reached_downloader")

    def run(self, spider_name):
        process_crawler = CrawlerProcess(scrapy_settings.__dict__)
        loader = process_crawler.spider_loader
        spider_cls = loader.load(spider_name)
        crawler = self.crawler_signals(Crawler(spider_cls, self.settings))
        process_crawler.crawl(crawler)
        process_crawler.start()


if __name__ == '__main__':
    m = MySpider()
    m.run(spider_name="baidu_spider")
