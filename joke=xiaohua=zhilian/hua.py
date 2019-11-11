# -*- coding: utf-8 -*-
import scrapy


class HuaSpider(scrapy.Spider):
    name = 'hua'
    allowed_domains = ['521609.com/daxuexiaohua/']
    start_urls = ['http://521609.com/daxuexiaohua//']

    def parse(self, response):
        pass
