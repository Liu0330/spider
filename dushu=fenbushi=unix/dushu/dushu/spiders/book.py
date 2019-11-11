# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ..items import DushuItem

class BookSpider(CrawlSpider):
    name = 'book'
    allowed_domains = ['dushu.com']
    # 世界名著的栏目里面的数据
    start_urls = ['https://www.dushu.com/']
    # 超链接提取的规则
    # 获取不同栏目图书，多页的图书
    rules = (
        Rule(LinkExtractor(allow=r'/book/[\d]+_[\d]+.html'), callback='parse_item', follow=True),
        Rule(LinkExtractor(restrict_xpaths='//div[@id="tab1"]/div[@class="class-nav"]/a'), callback='parse_item', follow=True),
    )
    def parse(self, response):
        books = response.xpath('//div[@class="bookslist"]/ul/li')
        print('-------------------------',len(books))
        # 第一页的内容
        fp = open('./page1.txt',mode='w',encoding='utf-8')
        for book in books:
            item = DushuItem()
            book_name = book.xpath('.//img/@alt').extract()[0]
            img_url = book.xpath('.//img/@src').get()
            book_author = book.xpath('.//p[1]/text()').get()
            book_info = book.xpath('.//p[2]/text()').extract()[0]
            item['img_url'] = img_url
            item['book_name'] = book_name
            item['book_author'] = book_author
            item['book_info'] = book_info
            # yield item#执行了yield 下面的代码不会执行了
            fp.write('%s,%s,%s,%s\n'%(img_url,book_name,book_author,book_info))
        fp.close()
        return super().parse(response)
    def parse_item(self, response):
        books = response.xpath('//div[@class="bookslist"]/ul/li')
        #item['domain_id'] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        for book in books:
            item = DushuItem()
            book_name = book.xpath('.//img/@alt').extract()[0]
            img_url = book.xpath('.//img/@src').get()
            book_author = book.xpath('.//p[1]//a/text()').get()
            book_info = book.xpath('.//p[2]/text()').extract()[0]

            item['img_url'] = img_url
            item['book_name'] = book_name
            item['book_author'] = book_author
            item['book_info'] = book_info
            yield item
