# -*- coding: utf-8 -*-

import urllib
from urllib import request
from urllib import parse
#测试get和post请求
url = 'http://httpbin.org/post'

if __name__ == '__main__':
    params = {
        'Language':'python',
        'salary': 20000,
        'worktime':996
    }
    params  = urllib.parse.urlencode(params).encode()
    response= urllib.request.urlopen(url=url, data=params) #ctrl alt v 提取 ctrl+p 提示
    print(response.read().decode())


