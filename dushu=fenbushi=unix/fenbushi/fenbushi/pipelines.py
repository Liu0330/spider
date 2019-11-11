# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class FenbushiPipeline(object):
    def open_spider(self,spider):
        self.fp = open('./books.txt',mode = 'w',encoding='utf-8')
        self.num = 0
    def process_item(self, item, spider):

        self.fp.write('%s,%s,%s,%s\n'%(item['img_url'],
                                       item['book_name'],
                                       item['book_author'],
                                       item['book_info']))
        self.num += 1
        print('-----------------------',self.num)
        return item
    def close_spider(self,spider):
        self.fp.close()
