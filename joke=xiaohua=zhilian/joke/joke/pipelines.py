# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class JokePipeline(object):
    def open_spider(self, spider):
        self.fp = open('./joke.txt', mode='a', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write('%s,%s\n' % (item['title'], item['href']))

    def close_spider(self, spider):
        self.fp.close()


class JokePipeline2(object):
    def open_spider(self, spider):
        self.fp = open('./joke2.txt', mode='a', encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write('%s,%s\n' % (item['title'], item['href']))

    def close_spider(self, spider):
        self.fp.close()
