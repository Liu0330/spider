# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieItem

class FilmSpider(scrapy.Spider):
    name = 'film'
    allowed_domains = ['dy2018.com']
    start_urls = ['https://www.dy2018.com/html/gndy/dyzz/index.html'] +\
                 ['https://www.dy2018.com/html/gndy/dyzz/index_%d.html'%(i) for i in range(2,308)]

    def parse(self, response):
        movies = response.xpath('//div[@class="co_content8"]/ul//table//a')
        print('-----------------------------',len(movies))
        for movie in movies:
            item = MovieItem()
            movie_detail = 'https://www.dy2018.com'+ movie.xpath('./@href').extract()[0]
            movie_title = movie.xpath('./@title').get()
            # 一级url中解析出来想要两个属性
            item['title'] = movie_title
            item['href'] = movie_detail
            print(item)
            # 发起新的Request
            yield scrapy.Request(movie_detail,callback=self.parse_movie_detail,meta={'item':item})

    def parse_movie_detail(self,response):
        # item中含有两个数据了
        item = response.meta['item']
        # 剩余的三个数据，继续解析
        post = response.xpath('//div[@id="Zoom"]//img/@src').get()

        infos = response.xpath('//div[@id="Zoom"]/p/text()').extract()
        print(post)
        import re
        # infos.re('[(*?)]')
        # info = response.selector.re('影片([\u4E00-\u9FA5A-Za-z0-9\s\S*?]+)$')

        try:
            index = infos.index('◎简\u3000\u3000介') + 1
        except:
            # pass
            index = infos.index('◎简\u3000\u3000介 \xa0\xa0') +1
        info = infos[index]
        print(info)
        download_url = response.xpath('//td[@bgcolor="#fdfddf"]/a/@href').get()
        print(download_url)
        item['post'] = post
        item['info'] = info
        item['download_url'] = download_url
        yield item
        # 影片简介：(*+)<br>