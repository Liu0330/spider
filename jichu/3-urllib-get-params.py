# -*- coding: utf-8 -*-

import urllib
from urllib import request
from urllib import parse
#测试get和post请求
url = 'http://httbin.org/get?%s'

if __name__ == '__main__':
    params = {"age":35,'sex':'男','work_years':'15'}
    params = urllib.parse.urlencode(params)
    response =urllib.request.urlopen(url = url%(params))
    print(response.read().decode())