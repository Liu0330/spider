# -*- coding: utf-8 -*-
import urllib
from urllib import request

if __name__ == '__main__':
    # Request请求
    url = "http://oa.1000phone.net/oa.php"
    headers = {
    # Accept: text / html, application / xhtml + xml, application / xml;q = 0.9, image / webp, image / apng, * / *;q = 0.8, application / signed - exchange; v = b3
    # Accept - Encoding: gzip, deflate
    # Accept - Language: zh - CN, zh; q = 0.9
    # Cache - Control: max - age = 0
    # Connection: keep - alive
    'Cookie':'PHPSESSID=ST-56995-8t1zsY2JpoqzcaRuLLlNvq5-Pks-izm5ejd5j1npj2pjc7i3v4z'
    # Host: oa.1000phone.net
    # Upgrade - Insecure - Requests: 1
    # User - Agent: Mozilla / 5.0(Windows NT10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 78.0.3904.70Safari / 537.36
    }
    request1 = request.Request(url=url)
    # 发起请求
    request1.add_header('Cookie','')
    response = urllib.request.urlopen(request1)

    # 打印网页数据
    print(response.read().decode('utf-8'))
