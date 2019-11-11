# -*- coding: utf-8 -*-
import requests
url = 'http://httpbin.org/post'

if __name__ == '__main__':
    response  = requests.post(url=url, data={'sex': 'male男', 'class': 'Python'})
    response.encoding = 'utf-8'
    print(response.text)

