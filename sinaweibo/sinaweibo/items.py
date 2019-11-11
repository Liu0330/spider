# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy



class SinaweiboItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()       #用户名
    first_news = scrapy.Field()     #首条微博
    dates = scrapy.Field()     #发布时间
    zhuanzai = scrapy.Field()       #转载数
    comment = scrapy.Field()        #评论数
    agree = scrapy.Field()      #点赞数
    city = scrapy.Field()       #所在地区
