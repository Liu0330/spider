# -*- coding: utf-8 -*-
import urllib
from urllib import request

if __name__ == '__main__':
    # response = urllib.request.urlopen(url = 'http://39.106.94.21/')
    # test = response.read().decode("utf-8")
    # with open('./baidu.html',mode='w',encoding='utf-8')as fp:
    #     fp.write(test)
    #     print("保存成功")

    picture  = "https://imgconvert.csdnimg.cn/aHR0cHM6Ly9pbWcyMDE4LmNuYmxvZ3MuY29tL2Jsb2cvMTcwMDk5Ny8yMDE5MDUvMTcwMDk5Ny0yMDE5MDUyOTE0MTIzMTc0OC00NjA2OTUxMTkucG5n?x-oss-process=image/format,png"
    response = urllib.request.urlopen(url = picture)
    test = response.read()
    with open('./test.jpg',mode='wb',)as fp:
        fp.write(test)
        print("保存图片成功")

