# -*- coding: utf-8 -*-
import scrapy
from sinaweibo.items import SinaweiboItem
import json
import re
import copy


class WeibodiyuSpider(scrapy.Spider):
    name = 'wb'  #爬虫名
    allowed_domains = ['m.weibo.cn']    #只在该域名内爬取
    start_urls = ['https://m.weibo.cn/api/container/getIndex?containerid=1076033267187212'
                  ]

    def parse1(self, response):
        infos = json.loads(response.body)   #将内容转为json对象
        item = response.meta['item']    #利用meta方法传入item
        city = response.meta['city']    #传入城市
        try:
            name = infos["data"]["cards"][0]["mblog"]["user"]["screen_name"]    #爬取名字
            first_news = re.findall('([\u4e00-\u9fa5]+)', str(infos["data"]["cards"][0]["mblog"]["text"]), re.S)    #爬取微博内容，使用正则去除一些杂项如网页代码
            dates = infos["data"]["cards"][0]["mblog"]["created_at"]    #发布时间
            zhuanzai = infos["data"]["cards"][0]["mblog"]["reposts_count"]    #转载数
            comment = infos["data"]["cards"][0]["mblog"]["comments_count"]    #评论数
            agree = infos["data"]["cards"][0]["mblog"]["attitudes_count"]    #点赞数
            #将数据赋给item
            item['name'] = name
            item['first_news'] = first_news
            item['dates'] = dates
            item['zhuanzai'] = zhuanzai
            item['comment'] = comment
            item['agree'] = agree
            item['city'] = city
            return item    #返回
        except IndexError or KeyError:
            pass

    def parse2(self, response):    #获取所在地区函数
        infos = json.loads(response.body)
        try:
            item = response.meta['item']    #传入item
            city_cont = str(infos["data"]["cards"][1]["card_group"])
            city = re.findall('card_type.*?所在地.*?item.*?:(.*?)}]', city_cont, re.S)[0].replace('\'', '').replace(
                ' ', '')    #城市
            item['city'] = city
            ids = response.meta['ids']    #传入id并赋给ids变量
            n_url1 = 'https://m.weibo.cn/api/container/getIndex?&containerid=107603' + ids
            yield scrapy.Request(n_url1, meta={'item': item, 'city': copy.deepcopy(city)}, callback=self.parse1)    #执行完上述命令后的步骤
        except IndexError or KeyError:
            pass

    def parse(self, response):
        datas = json.loads(response.body)
        item = SinaweiboItem()
        for i in range(0, 20):
            try:
                ids = str(datas["data"]["cards"][i]["mblog"]["user"]["id"])    #获取用户id
                n_url2 = 'https://m.weibo.cn/api/container/getIndex?containerid=230283{}_-_INFO'.format(ids)
                yield scrapy.Request(n_url2, meta={'item': item, 'ids': copy.deepcopy(ids)}, callback=self.parse2)    #进入parse2函数执行命令
            except IndexError or KeyError:
                pass
        social_urls = [
            'https://m.weibo.cn/api/container/getIndex?containerid=102803_ctg1_4188_-_ctg1_4188&openApp=0&since_id={}'.format(
                str(i)) for i in range(2, 100)]
        celebritys_urls = [
            'https://m.weibo.cn/api/container/getIndex?containerid=102803_ctg1_4288_-_ctg1_4288&openApp=0&since_id={}'.format(
                str(j)) for j in range(1, 100)]
        hots_urls = ['https://m.weibo.cn/api/container/getIndex?containerid=102803&openApp=0&since_id={}'.format(str(t))
                     for
                     t in range(1, 100)]
        urls = celebritys_urls + social_urls + hots_urls    #入口网址
        for url in urls:
            yield scrapy.Request(url, callback=self.parse)