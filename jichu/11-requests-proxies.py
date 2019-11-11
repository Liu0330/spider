import requests

url = 'http://httpbin.org/ip'

if __name__ == '__main__':
    # 私密代理，需要使用，用户名和密码
    response = requests.get(url=url,proxies = {'http':'http://455098435:lbrv3bgb@121.42.140.113:16816'},timeout = 20)
    print(response.text)