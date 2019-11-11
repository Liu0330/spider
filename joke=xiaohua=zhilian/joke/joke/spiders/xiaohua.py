# -*- coding: utf-8 -*-
import scrapy
from  ..items import JokeItem

class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    allowed_domains = ['xiaohua.zol.com.cn']
    start_urls = ['http://xiaohua.zol.com.cn/']

    def start_requests(self):
        return super().start_requests()

    def parse(self, response):
        jokes =response.xpath('//ul[@class="news-list video-list"]/li/a')
        print('--------',len(jokes))
        for joke in jokes:
            item =JokeItem()
            title = joke.xpath('./@title')[0].extract()
            href = 'http://xiaohua.zol.com.cn'+joke.xpath('./@href').get()
            item['title'] =title
            item['href'] =href
            print('-'*50,title,href)
            # yield item,返回条目管道存数据
            yield scrapy.Request(href,callback=self.parse_joke_detail,meta={'item':item})

    def parse_joke_detail(self,response):
        item = response.meta['item']
        content = response.xpath('//div[@class="article-text"]/p/text()').extract()
        print('content:', content)
        item['content'] =content
        yield item

