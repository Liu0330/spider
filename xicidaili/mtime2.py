import requests
import time
import json
from lxml import etree

#获取页面的html并返回etree
def get_html_tree(url,headers):
    resp = requests.get(url,headers=headers).text
    resp.encode('utf-8')
    resp_tree = etree.HTML(resp)
    return resp_tree

#获取初始页的电影链接
def get_movie_link(resp_tree):
    links = resp_tree.xpath('//div[@class="mov_con"]//h2/a/@href')
    return links

#对每个电影页面进行解析
def parse_page(movie_tree,movie_id):
    #从json中获取电影评分
    surl = 'http://service.library.mtime.com/Movie.api?Ajax_CallBack=true&Ajax_CallBackType=Mtime.Library.Services&Ajax_CallBackMethod=GetMovieOverviewRating&Ajax_CrossDomain=1&Ajax_RequestUrl=http%3A%2F%2Fmovie.mtime.com%2F'+movie_id+'%2F&Ajax_CallBackArgument0='+movie_id
    sresp = requests.get(surl,headers=headers)
    b = sresp.text.find('MovieId')
    e = sresp.text.find('IP":0')
    sjson = json.loads(sresp.text[b-2:e+6])
    s = sjson['RatingFinal']
    #获取电影名称，年份和内容简介
    name = movie_tree.xpath('//div[@class="db_head"]//h1/text()')
    year = movie_tree.xpath('//div[@class="db_head"]//p/a/text()')
    content = movie_tree.xpath('//*[@id="movie_warp"]//dl/dt/p[1]/text()')
    return name,s,year,content

#获取下一页的链接
def get_page_links(resp_tree):
    all_page_links = resp_tree.xpath('//*[@id="PageNavigator"]/a/@href')
    return all_page_links

def main():
    global headers
    url = 'http://www.mtime.com/top/movie/top100/'
    headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36'}
    top = 1
    for page in range(2,12):
        resp_tree = get_html_tree(url,headers)
        links = get_movie_link(resp_tree)
        for link in links:
            try:
                movie_tree = get_html_tree(link,headers)
                movie_id = str(link)[23:-1]
                movie=parse_page(movie_tree,movie_id)
                print('%d:' %top, '电影名称：%s' %movie[0])
                print('评分：%s' %movie[1])
                print('年代：%s' %movie[2])
                print('内容介绍：%s' %movie[3])
                top += 1
            except Exception as e :
                print('-'*100,e)
        url = 'http://www.mtime.com/top/movie/top100/index-%d.html' %page

if __name__ == '__main__':
    main()
