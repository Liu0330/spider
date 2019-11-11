# -*- coding: utf-8 -*-

import re
import threading
import urllib
import requests
from urllib import request

#获取视频名称的id
def get_urls():
    global urls
    url = 'https://api-m.mtime.cn/PageSubArea/HotPlayMovies.api?sign=864de2fcca3230a577aa3294639a805b&locationId=515'
    urls = []
    urls.append(url)
    response = requests.get(url)
    response.encoding = 'utf-8'
    content = response.text
    # print(content)
    ids = re.findall(r'"movieId":(.*?),"', content)
    names = re.findall(r'"commonSpecial":(.*?),"', content)
    print(ids,names)
    return ids,names

#获取视频的url和名
def get_movieurls(ids,names):
        n=0
        for id  in ids :
            print(names[n])
            url_movieid = 'https://api-m.mtime.cn/Movie/Video.api?movieId=%s&pageIndex=1'%id
            print(url_movieid)
            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36', }

            response = requests.get(url_movieid,headers = headers)
            response.encoding = 'utf-8'
            content = response.text

            movie_mp4_url = re.findall(r'"hightUrl":(.*?),"', content)
            movie_mp4_title = re.findall(r'"title":(.*?)",', content)
            # print(movie_mp4_url,movie_mp4_title)
            # 创建线程

            t = threading.Thread(target=down_movie, args=(movie_mp4_title, movie_mp4_url))
            # t.start()
            threads.append(t)
            # down_movie(movie_mp4_title, movie_mp4_url)
            n+=1


#下载视频
def down_movie(movie_mp4_title, movie_mp4_url):
    i = 0
    for url in movie_mp4_url:
        print('<< %s >>开始下载…………' % movie_mp4_title[i])
        print(url)
        # urllib.request.urlretrieve(url=url, filename='./%s.mp4'%movie_mp4_title[i])
        print('视频保存成功！')
        i += 1




if __name__ == '__main__':

    #获取热映视频的ids
    ids, names = get_urls()
    #获取视频id内容的每个具体视频和标题
    threads = []
    get_movieurls(ids,names)
    for t in threads:
    #创建多进程
        t.start()
        # threads.append(t)
        # join必须单独写，目的：线程启动否则io错误close原因
    for t in threads:
        t.join()
    # milt_threads()




