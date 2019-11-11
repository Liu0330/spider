# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import FenbushiItem
class BookSpider(RedisCrawlSpider):
    name = 'book'
    allowed_domains = ['dushu.com']
    # start_urls = ['http://dushu.com/']
    redis_key = 'start_url'
    rules = (
        Rule(LinkExtractor(allow=r'/book/[\d]+_[\d]+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="tab1"]/div[@class="class-nav"]/a'), callback='parse_item',
             follow=True),
    )
    def parse_item(self, response):
        books = response.xpath('//div[@class="bookslist"]/ul/li')
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        for book in books:
            item = FenbushiItem()
            book_name = book.xpath('.//img/@alt').extract()[0]
            img_url = book.xpath('.//img/@src').get()
            book_author = book.xpath('.//p[1]/text()').get()
            book_info = book.xpath('.//p[2]/text()').extract()[0]
            item['img_url'] = img_url
            item['book_name'] = book_name
            item['book_author'] = book_author
            item['book_info'] = book_info
            yield item
