# -*- coding: utf-8 -*-
import scrapy
import re


class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    start_urls = ['http://www.renren.com/511563151/profile']


    def start_requests(self):
        cookies = "anonymid=jvevv94ix9yqdh; depovince=GW; _r01_=1; JSESSIONID=abcPKEZYsEGA7cpw2rwQw; ick_login=87b7a2fb-dd8f-4fc5-82c2-c220ab5b0ff9; wp_fold=0; XNESSESSIONID=6a48b56f9abb; jebecookies=ed16ade2-902a-47a1-959d-1e8049fdea41|||||; _de=8D11F1C5CAD27BD9158AF465F3185AA1; p=61362c72ac6fd42f25768f911ec1d34f1; first_login_flag=1; ln_uact=13718488977; ln_hurl=http://hdn.xnimg.cn/photos/hdn321/20150728/2225/h_main_3wSE_49360001982d1986.jpg; t=83f71085bc61eb3abf131fb01837e35b1; societyguester=83f71085bc61eb3abf131fb01837e35b1; id=511563151; xnsid=69b3a9db; ver=7.0; loginfrom=null; wp=0"
        cookies ={i.split("=")[0]:i.split("=")[1] for i in cookies.split(";")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )


    def parse(self, response):
        print(re.findall("刘旺",response.body.decode()))
        yield scrapy.Request(
            "http://www.renren.com/511563151/profile?v=info_timeline",
            callback =self.parse_detail
        )
    def parse_detail(self,response):
        print(re.findall("刘旺", response.body.decode()))
