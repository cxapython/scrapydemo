# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class BaiDuSpider(scrapy.Spider):
    name = 'baidu_spider'

    def start_requests(self):
        url = "https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=request_reached_downloader"
        yield Request(url, dont_filter=True, callback=self.parse)

    def parse(self, response):
        data_list = response.xpath("//div[@id='content_left']/div[@mu]")

        for each_item in data_list:
            item = {}
            url = each_item.xpath(".//@mu").get("").strip()
            title = each_item.xpath(".//h3/a/text()").get("").strip()
            if not title:
                continue
            item["link_url"] = url
            item["title"] = title
            yield item
