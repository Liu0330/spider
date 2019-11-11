# -*- coding: utf-8 -*-
import scrapy
import re

class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        #大分类分组
        li_list = response.xpath("//div[@class='menu-list'/dl/dt" )
        for li in li_list:
            item = {}
            item["b_cate"] = li.xpath("./dd[0]/a/text()").extract_firt()
            a_list = li.xpath(".div[2]/a")
            for a in a_list:
                item["s_href"] = a.xpath("./@href").extract_first()
                item["s_cate"] = a.xpath("./text()").extract_first()
                if item["s_href"] is not None:
                    item["s_href"] = "http://list.suning.com/"+item["s_href"]
                    yield scrapy.Request(
                        item["s_href"],
                        callback  = self.parse_book_list,
                        meta = {"item":item}
                    )
    def parse_book_list(self,response):
        item = response.meta["item"]
        li_list = response.xpath("//div[@class='filtrate-books list-filtratebooks']/ul/li")
        for li in li_list:
            item["book_name"] = li.xpath(".//div[@class='book-title'/a/@title]").extract_first()
            item["book_img"] = li.xpath(".//div[@class='book-title'/a/@title]").extract_first()
            item["book_author"] = li.xpath(".//div[@class='book-title'/a/@title]").extract_first()
            item["book_publish"] = li.xpath(".//div[@class='book-title'/a/@title]").extract_first()
            item["book_descrip"] = li.xpath(".//div[@class='book-title'/a/@title]").extract_first()
            item["book_href"] = li.xpath(".//div[@class='book-title'/a/@href]").extract_first()

            yield scrapy.Request(
                    item["book_href"],
                    callback=self.parse_book_datail,
                    meta={"item": item}
                )

    def parse_book_datail(self, response):
        item = response.meta["item"]
        item["book_price"] = re.findall("\"bp\":'(.*?)',",response.body.decode())
        item["book_price"] =item["book_price"][0] if len(item["book_price"])>0 else None
        print(item)

