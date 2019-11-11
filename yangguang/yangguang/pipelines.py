# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import re
from yangguang.settings import MONGO_HOST
from  pymongo import MongoClient

class YangguangPipeline(object):
    def open_spider(self,spider):
        spider.hello = "world"
        client = MongoClient()
        self.collection  = client["test"]["test"]

    def process_item(self, item, spider):
        item["content"] = self.process_content(item["content"])
        print(item)

        self.collection.insert(dict(item))
        return item

    def process_content(self,content):
        content = [re.sub("r\xa0|\s","",i)for i in content]
        content = [i for i in content if len(i)>0]#去除列表中的空字符串
        return content
