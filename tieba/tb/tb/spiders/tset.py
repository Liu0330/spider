# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
import requests


class TsetSpider(CrawlSpider):
    name = 'tset'
    allowed_domains = ['zhipin.com']
    start_urls = ['https://www.zhipin.com/c101010100-p100109/?ka=sel-city-101010100/']

    def parse(self, response):
        # print(response.text)
        item = {}
        item["title"] = response.xpath("//div[@class='name']").extract_first()
        item["aquire"] = response.xpath("//div[@class='msg']").extract_first()
        # return i
        print(item)