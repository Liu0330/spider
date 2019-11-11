import urllib
from urllib import request
from urllib import response
# 免费，西刺代理

if __name__ == '__main__':
    url = 'http://httpbin.org/ip'
    # 不适用代理发起请求
    response = urllib.request.urlopen(url = url)
    print(response.read().decode())

    # 使用代理，伪装，爬虫，封id
    ph = urllib.request.ProxyHandler({'http':'117.69.201.206:9999'})
    # 打开者，打开url
    opener = urllib.request.build_opener(ph)
    # 使用代理打开一个网址
    response2 = opener.open(url)
    print('使用代理，ip是：',response2.read().decode())
    # print(response.getcode())#相应码200,304 404
    # print(response.geturl())