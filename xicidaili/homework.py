# -*- coding: utf-8 -*-
import threading

import requests
from lxml import etree

def download(img_url):
    response = requests.get(img_url)
    response.encoding = 'utf-8'
    content = response.text
    html = etree.HTML(content)
    result = html.xpath('//div[@class="indent"]/table')
    # print(len(result))
    for li in result:
        try:
            title = li.xpath('.//div[@class="pl2"]/a/text()')[0].strip().strip('\n')
            print(title)
            author = li.xpath('.//p[@class="pl"]/text()')[0].strip().strip('\n')
            print(author)
            info = ''.join(li.xpath('.//p[@class="quote"]/span/text()'))
            print(info)
            fp.write('%s\t%s\t%s \n\n' % (title, author, info))
        except Exception as e:
            # 异常保存，第二天，分析，单独爬取。
            print(e)


def get_urls():
    global urls
    url = 'https://book.douban.com/top250?start=%s'
    urls = []
    for i in range(0, 11):
        url_top = url % (i * 25)
        urls.append(url_top)
    # print(urls)


def milt_threads():
    threads = []
    for img_url in urls:
        t = threading.Thread(target=download, args=(img_url,))
        t.start()
        threads.append(t)
    # join必须单独写，目的：线程启动否则io错误close原因
    for t in threads:
        t.join()


if __name__ == '__main__':
    fp = open('./doubanbooktop.csv',mode = 'a',encoding='utf-8')
    #获取urls
    get_urls()
    #创建多进程
    milt_threads()

    fp.close()


