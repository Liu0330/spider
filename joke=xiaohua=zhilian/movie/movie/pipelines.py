# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


class MoviePipeline(object):
    def open_spider(self,spider):
        self.fp = open('./movie.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        self.fp.write('%s\t%s\t%s\t%s\t%s\t\n'%(item['title'],item['href'],item['post'],item['info'],item['download_url'],))

        return item


    def close_spider(self, spider):
        self.fp.close()