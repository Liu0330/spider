# -*- coding: utf-8 -*-
import requests
if __name__ == '__main__':
    response = requests.get(url = 'http://www.baidu.com/')
    response.encoding = 'utf-8'

    print(response.text)
