# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class Tt1Spider(CrawlSpider):
    name = 'tt1'
    allowed_domains = ['tencent.com']
    start_urls = ['https://hr.tencent.com/position.php/']

    rules = (
        #提取翻页列表页的URL地址
        Rule(LinkExtractor(allow=r'position\.php\?&start=\d+#a'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        tr_list = response.xpath("//table[@class='tablelist']/tr")[1:-1]
        for tr in tr_list:
            item = {}
            item["title"] = tr.xpath("./td[1]/a/text()").extract_first()
            item["href"] = "https://hr.tencent.com/"+tr.xpath("./td[1]/a/@href").extract_first()
            yield scrapy.Request(
                item["href"],
                callback=self.parse_detail,
                meta = {"item":item}
            )

    def parse_detail(self,response):
        item = response.meta["item"]
        item["aquire"] = response.xpath("//div[text()='工作要求：']/../ul/li/text()").extract()
        print(item)