# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

import pymysql
class DushuPipeline(object):
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host = 'localhost',port = 3306,
                user = 'root',password = 'liuwang',
                database = 'books_gp02',charset='utf8')
        self.cursor = self.conn.cursor()
    def process_item(self, item, spider):
        sql = 'insert into book(book_url,book_name,book_author,book_info) ' \
                 'values("%s","%s","%s","%s")' % (item['img_url'],
                                                  item['book_name'],
                                                  item['book_author'],
                                                  item['book_info'])
        self.cursor.execute(sql)
        self.conn.commit()#提交
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()