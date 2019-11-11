import requests

url = 'http://oa.1000phone.net/oa.php/Expense/index'

if __name__ == '__main__':
    # 联网请求的会话
    sess = requests.Session()
    # 通过会话获取首页的数据，验证，cookies，会话记住
    cookies = {'PHPSESSID': 'ST-56995-8t1zsY2JpoqzcaRuLLlNvq5-Pks-izm5ejd5j1npj2pjc7i3v4z'}
    re = sess.get(url = 'http://oa.1000phone.net/oa.php', cookies =cookies)

    # 使用会话发起新的url的请求
    response = sess.get(url,cookies = cookies)
    print(response.text)