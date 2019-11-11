# -*- coding: utf-8 -*-
import scrapy


class ChinaunixSpider(scrapy.Spider):
    name = 'chinaunix'
    allowed_domains = ['account.chinaunix.net','bbs.chinaunix.net']
    start_urls = ['http://account.chinaunix.net/login/login']
    # 定制了post请求
    def start_requests(self):
        form = {'username':'18513106743',
                'password':'31415926abc',
                '_token':'bKZYAlnH',
                '_t':'1572848242163'}
        print('+++++++++++++++++++++++发起post请求')
        yield scrapy.FormRequest(url = self.start_urls[0],
                                  formdata=form,
                                  callback=self.parse_post)

    # 已经登录了，cookies，意味着，可以获取网站，详情数据,发起get请求可以了
    def parse_post(self, response):
        url = 'http://bbs.chinaunix.net/'
        print('-------------------------',response.body.decode('utf-8'))
        print('-------------------------',response.status)
        yield scrapy.Request(url = url,callback=self.parse_bbs)
    def parse_bbs(self,response):
        content = response.body.decode('gbk')
        with open('./bbs.html',mode='w',encoding='gbk') as fp:
            fp.write(content)