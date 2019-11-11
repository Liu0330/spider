# -*- coding: utf-8 -*-
import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']     #允许爬取的范围
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml'] #最开始请求的url地址

    def parse(self, response):
        #处理start_url地址的响应
        # ret = response.xpath('//div[@class="tea_con"]//h3/text()').extract()
        # print(ret)

        li_list= response.xpath('//div[@class="tea_con"]//li')
        for li in li_list:
            item = {}
            item["name"] = li.xpath(".//h3/text()").extract_first()
            item["title"] = li.xpath(".//h4/text()").extract_first()
            # print(item)
            yield  item