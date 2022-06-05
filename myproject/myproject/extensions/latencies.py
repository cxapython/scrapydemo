# -*- coding: utf-8 -*-
# @Time : 2022/6/5 6:22 下午
# @Author : chenxiangan
# @File : latencies.py
# @Software: PyCharm
from time import time

from scrapy import signals
from scrapy.exceptions import NotConfigured
from twisted.internet import task


class Latencies(object):
    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    def __init__(self, crawler):
        self.crawler = crawler
        self.interval = crawler.settings.getfloat('LATENCIES_INTERVAL')
        if not self.interval:
            raise NotConfigured
        cs = crawler.signals
        cs.connect(self._spider_opened, signal=signals.spider_opened)
        cs.connect(self._spider_closed, signal=signals.spider_closed)
        #当一个引擎从调度器取走一个request对象的时候触发request_scheduled。
        cs.connect(self._request_scheduled, signal=signals.request_scheduled)
        cs.connect(self._response_received, signal=signals.response_received)
        cs.connect(self._item_scraped, signal=signals.item_scraped)
        self.latency, self.proc_latency, self.items = 0, 0, 0

    def _spider_opened(self, spider):
        self.task = task.LoopingCall(self._log, spider)
        # 爬虫开始后self.interval秒后开始执行self._log方法
        self.task.start(self.interval)

    def _spider_closed(self, spider, reason):
        if self.task.running:
            self.task.stop()

    def _request_scheduled(self, request, spider):
        # schedule_time：记录爬虫开始的时间
        request.meta['schedule_time'] = time()

    def _response_received(self, response, request, spider):
        # response_time：记录引擎从downloader获取response对象的时间
        request.meta['received_time'] = time()

    def _item_scraped(self, item, response, spider):
        # self.latency：记录从调度器取走请求对象到item被数据库存储所用的时间
        self.latency += time() - response.meta['schedule_time']
        # self.proc_latency：记录响应经过爬虫中间件、spider、item pipeline所用的时间
        self.proc_latency += time() - response.meta['received_time']
        # 当有一个item被存储时，self.items数量加一
        self.items += 1

    def _log(self, spider):
        # irate：记录self.interval秒内的平均每秒爬多少的item。
        irate = float(self.items) / self.interval
        # latency：记录self.interval秒内平均每个item从调度器提出请求到item被数据库保存，所用的时间
        latency = self.latency / self.items if self.items else 0
        # proc_latency：记录self.interval秒内每个item响应经过爬虫中间件、spider、item pipeline所用的时间
        proc_latency = self.proc_latency / self.items if self.items else 0
        # 将爬取的信息放到日志中
        spider.logger.info(
            ("Scraped %d items at %.1f items/s, avglatency: ""%.2f s and avg time in pipelines: %.2f s") %
            (self.items, irate, latency, proc_latency))
        self.latency, self.proc_latency, self.items = 0, 0, 0

