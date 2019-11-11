import requests
import time
import re

url = 'http://account.chinaunix.net/login/login'
if __name__ == '__main__':
    t = int(time.time() * 1000)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Cookie': '__backurl=http%3A%2F%2Fbbs.chinaunix.net%2F; pgv_pvi=8022112440; pgv_pvid=9818425225; __utma=225341893.681452405.1528180059.1550043987.1569333916.4; __utmz=225341893.1569333916.4.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; ucenter_token=589dVCfYfwkTWAs%2FMRO%2FejkiYA6bX93PjXOqT%2FIrncIyWVKty9bNzkdd8HL%2F2INZJky2stfUwO4rCquZIpIdJn7%2Fr2A542Wzk%2F3CEgISSz2rxHbq4j0Gfxx2%2FF2oMLHm4tFt5CL7bHPhNBBPI4Hk4ce4E2qp7rzAwk9cSr8xmCgdD8G5zXQDMXhMHV98zubGvuqlQ6UEJtz80wdWPZ35i2wqnRkUX%2BVSkMagNZbiPHt4ZgjdOlzwUK7APjOxNoH8%2Fi6rsmKYRUkE%2BAXmlaV1RntSjTO7iFaIKyDk%2Bumiwz0%2Bp97%2B7eNipoVpfeiuqFuFLhzAUjRlpUj%2B%2FmvF4LInVo9GUwas83xpXR0lqm8AvvxFqkZnl2NRFDJuYgxf4EwyrTub02HBOg9j9YRWD%2BTofk5nJ7Bmr28FaQRLgFRjgP8wJGdg7lg; account_chinauni=accountchinauni; XSRF-TOKEN=4uxOsTVMWoiUkx7voP3oR82Z47dgzJasQKzxopCm; laravel_session=jEjNGC4rMYS7N45KNykCWNL12mFDB3E3zWFDe4nH; pgv_info=ssi=s4132952996; __pts=460014922; __ptb=460014922; Hm_lvt_0ee5e8cdc4d43389b3d1bfd76e83216b=1572275726,1572311774; st_user_token=940335ca0feedd548224a10d82235138; __pta=331961500.1527991916.1572312533.1572312748.5; Hm_lpvt_0ee5e8cdc4d43389b3d1bfd76e83216b=1572312748; captcha_gee=5db79784ac580',
        'Host': 'account.chinaunix.net',
        'Proxy-Connection': 'keep-alive',
        'Referer': 'http://bbs.chinaunix.net/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36', }
    # js动态代码没有办法进行模拟
    r = requests.get('http://account.chinaunix.net/login/',
                     headers = headers)
    '''<input type="hidden" name="_token" value="sXCa64MilB3YJWLTB0geRgobjVvU9RTtaIvCFtUE">'''
    content = r.text
    token = re.findall(r'name="_token" value="(.*?)">', content)
    print(token)
    params = {'username': 18513106743,
              'password': '31415926abc',
              '_token': token[0],
              '_t': t}
    # 使用会话发起了post请求
    sess = requests.Session()
    r = sess.post(url=url, data=params)
    print(r.text)
    # 会话记录Cookies，该网站其他页面可以访问了
    url = 'http://bbs.chinaunix.net/'
    response = sess.get(url=url)
    # print(response.text)
