# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
import scrapy


class BaiDuItem(scrapy.Item):
    # define the fields for your item here like:
    _id = scrapy.Field()
    link_url = scrapy.Field()
    title = scrapy.Field()
    web_site = scrapy.Field()