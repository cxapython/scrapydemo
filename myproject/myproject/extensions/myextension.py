# coding: utf-8
import time

from scrapy import signals

class MyExtension:
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def __init__(self, crawler):
        crawler.signals.connect(self.check_close, signal=signals.spider_closed)

    def check_close(self, spider, reason):
        stats = spider.crawler.stats.get_stats()
        item_scraped_count = stats.get("item_scraped_count", 0)
        print(f"爬虫结束抓取数据{item_scraped_count}条")

