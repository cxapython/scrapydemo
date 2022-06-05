# -*- coding: utf-8 -*-
# @Time : 2021/10/26 4:46 下午
# @Author : chenxiangan
# @File : mongo_pipeline.py
# @Software: PyCharm
import pymongo

db_configs = {
    'type': 'mongo',
    'host': '127.0.0.1',
    'port': '27017',
    "user": "",
    "password": "",
    'db_name': 'myprojectdb'
}


class MongoPipeline():
    def __init__(self):
        self.db_name = db_configs.get("db_name")
        self.host = db_configs.get("host")
        self.port = db_configs.get("port")
        self.username = db_configs.get("user")
        self.password = db_configs.get("passwd")

    def open_spider(self, spider):
        self.client = pymongo.MongoClient('mongodb://{}:{}'.format(self.host, self.port), connect=False, maxPoolSize=10)
        if self.username and self.password:
            self.db = self.client[self.db_name].authenticate(self.username, self.password)
        self.db = self.client[self.db_name]

    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        collection_name = spider.name
        # update_key = "object_id"
        # if not item.get("object_id"):
        #     update_key = "url"
        # if not item.get("url"):
        #     update_key = "link_url"
        # self.db[collection_name].update_one({update_key: item[update_key]}, {'$set': item}, upsert=True)
        print(f"插入到mongo的数据为:{item}")
        self.db[collection_name].insert_one(item)
        return item
