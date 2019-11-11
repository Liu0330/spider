# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import logging
logger = logging.basicConfig(...)  #设置日志输出的样式 格式

class MyspiderPipeline(object):
    def process_item(self, item, spider):

        print(item)
        return item