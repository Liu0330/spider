import requests

url = 'http://oa.1000phone.net/oa.php'
if __name__ == '__main__':
    '''PHPSESSID=ST-56995-8t1zsY2JpoqzcaRuLLlNvq5-Pks-izm5ejd5j1npj2pjc7i3v4z'''
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'PHPSESSID=ST-56995-8t1zsY2JpoqzcaRuLLlNvq5-Pks-izm5ejd5j1npj2pjc7i3v4z',
        'Host': 'oa.1000phone.net',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36', }
    # response = requests.get(url=url,
    #                         cookies={'PHPSESSID': 'ST-56995-8t1zsY2JpoqzcaRuLLlNvq5-Pks-izm5ejd5j1npj2pjc7i3v4z'})
    response = requests.get(url, headers=headers)
    print(response.text)
