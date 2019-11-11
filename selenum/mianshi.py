import threading

import requests
from lxml import etree


# 将网页的电影名称以及链接保存到movie.txt
def get_movie_url(movie_url):
    print(movie_url)
    response = requests.get(movie_url)
    # print(response.encoding)
    response.encoding = 'gbk'
    content = response.text
    # print(content)
    html = etree.HTML(content)

    result = html.xpath('//div[@class="co_content8"]//table')
    print(len(result))
    # xpath筛选table中的内容
    for li in result:
        try:
            title = li.xpath('.//b/a/text()')[1].strip().strip('\n')
            print(title)
            author = li.xpath('.//b/a/@href')[1].strip().strip('\n')
            print("https://www.dytt8.net/" + author)
            author = "https://www.dytt8.net" + author
            info = ''.join(li.xpath('.//tr/td/text()')[-1])
            print(info)
            fp.write('%s\t%s\n%s \n\n\n' % (title, author, info))
            fp1.write('%s\n%s\n' % (title, author))
        except Exception as e:
            # 异常保存，第二天，分析，单独爬取。
            print(e)


# 获取urls
def get_urls():
    global urls
    # url为国内电影
    url = 'https://www.dytt8.net/html/gndy/china/list_4_%s.html'
    urls = []
    # 提前看到国产电影有121页面
    for i in range(1, 121):
        url_top = url % (i)
        urls.append(url_top)


# 创建多线程 每个url一个线程
def milt_threads():
    threads = []
    for movie_url in urls:
        t = threading.Thread(target=get_movie_url, args=(movie_url,))
        t.start()
        threads.append(t)
    # join必须单独写，目的：线程启动否则io错误close原因
    for t in threads:
        t.join()


def download_movie():
    pass


if __name__ == '__main__':
    fp = open('./url.txt', mode='w', encoding='utf-8')
    fp1 = open('./movieurl.txt', mode='w', encoding='utf-8')
    # 获取urls
    get_urls()
    # 创建多进程
    milt_threads()
    fp.close()
    print('多线程科学获取所有国产电影内容及链接')
