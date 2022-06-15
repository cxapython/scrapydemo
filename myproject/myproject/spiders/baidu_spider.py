# -*- coding: utf-8 -*-
import asyncio

import scrapy
from scrapy import Request
from twisted.internet import reactor
from twisted.internet.defer import Deferred

from myproject.itemloader.myitemloader import MyItemLoader
from myproject.items.items import BaiDuItem


class BaiDuSpider(scrapy.Spider):
    name = 'baidu_spider'
    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
    }
    def start_requests(self):
        url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=request_reached_downloader"
        meta = {
            "web_site": "baidu",
            "time": 5,
            "callback": self.parse,
        }
        # yield Request(url,headers=self.headers, dont_filter=True, meta=meta, callback=self.request_with_pause)
        yield Request(url,headers=self.headers, dont_filter=True, meta=meta, callback=self.parse)

    def parse_item(self, selector, response):
        """
        itemoader的使用
        :param self:
        :param response:
        :return:
        """
        l = MyItemLoader(item=BaiDuItem(), selector=selector)
        l.add_value("web_site", response.meta.get("web_site"))
        l.add_xpath("link_url", ".//@mu")
        l.add_xpath("title",".//h3/a/text()")
        return l.load_item()



    def request_with_pause(self, response):
        d = Deferred()
        reactor.callLater(response.meta['time'], d.callback, Request(
            response.url,
            headers=self.headers,
            callback=response.meta['callback'],
            dont_filter=True))
        return d
    async def parse(self,response):
        data_list = response.xpath("//div[@id='content_left']/div[@mu]")

        for selector in data_list:
            await asyncio.sleep(5)
            yield self.parse_item(selector, response)
    # def parse(self, response):
    #     data_list = response.xpath("//div[@id='content_left']/div[@mu]")
    #
    #     # 1.普通方法
    #     # for each_item in data_list:
    #     #     item = {}
    #     #     url = each_item.xpath(".//@mu").get("").strip()
    #     #     title = each_item.xpath(".//h3/a/text()").get("").strip()
    #     #     if not title:
    #     #         continue
    #     #     item["link_url"] = url
    #     #     item["title"] = title
    #     #     item.add_value("website",response.meta['title'])
    #     #     yield item
    #
    #     #2.使用自定义itemloader的形式
    #     for selector in data_list:
    #         yield self.parse_item(selector, response)


