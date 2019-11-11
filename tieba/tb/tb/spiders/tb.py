# -*- coding: utf-8 -*-
import scrapy
import urllib
import requests

class TbSpider(scrapy.Spider):
    name = 'tb'
    allowed_domains = ['tieba.baidu.com']
    start_urls = ['http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw=%E6%9D%8E%E6%AF%85&lp=9001']

    def parse(self, response):
        #根据帖子进行分组
        div_list = response.xpath("//div[contains(@class,'i')]")
        for div in div_list:
            item = {}
            item["href"] = div.xpath("./a/@href").extract_first()
            item["title"] = div.xpath("./a/text()").extract_first()
            item["img_list"] = []
            if item["href"] is not None:
                item["href"] = urllib.parse.urljoin(response.url,item["href"])
                yield scrapy.Request(
                    item["href"],
                    callback=self.parse_detail,
                    meta = {"item":item}
                )
        #列表页的翻页
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_url is not None:
            next_url = urllib.parse.urljoin(response.url,next_url)
            yield scrapy.Request(
                next_url,
                callback=self.parse,
            )

    def parse_detail(self,response):
        item = response.meta["item"]
        # if "img_list" not in item:
        #     item["img_list"] = response.xpath("//img[@class='BDE_Image']/@src").extract()
        # else:
        item["img_list"].extend(response.xpath("//img[@class='BDE_Image']/@src").extract())
        next_url = response.xpath("//a[text()='下一页']/@href").extract_first()
        if next_url is not None:  #表示由下一页
            next_url = urllib.parse.urljoin(response.url,next_url)
            yield  scrapy.Request(
                next_url,
                callback=self.parse_detail,
                meta={"item":item}
            )
        else:
            item["img_list"] = [requests.utils.unquote(i).split("src=")[-1] for i in item["img_list"]]
            print(item)
            # yield item