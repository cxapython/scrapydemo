# -*- coding: utf-8 -*-
# @Time : 2022/6/5 3:39 下午
# @Author : chenxiangan
# @File : myitemloader.py
# @Software: PyCharm
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class MyItemLoader(ItemLoader):
    # 自定义 itemloader
    default_output_processor = TakeFirst()