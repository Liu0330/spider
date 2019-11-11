import re
import requests
import time
import random
import threading

url = 'https://www.xicidaili.com/nn/%d'
def get_proxies(proxies):
    host,port,protocol = random.choice(proxies)
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEkiJWMwMTk0MjI3Y2U0YzNlMzAxYTE2OTNhNzNjYWE5MjY4BjsAVEkiEF9jc3JmX3Rva2VuBjsARkkiMUQ2MFgwNjRkMW1TeWU4aW5Rc0ZFRUJTUWcySFQ5SkVESW4vNDFBM0o5YVk9BjsARg%3D%3D--4f5347e38cc48fa105784ff3eb74da208c89e3dc; Hm_lvt_0cf76c77469e965d2957f0553e6ecf59=1572194359,1572248969,1572272353,1572320920; Hm_lpvt_0cf76c77469e965d2957f0553e6ecf59=1572320946',
        'Host': 'www.xicidaili.com',
        'If-None-Match': 'W/"3caa2430052219a3e8d311f50f38de44"',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'none',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36', }
    fp = open('./proxies.txt', mode='a', encoding='utf-8')
    for i in range(10, 20):
        response = requests.get(url=url % (i),
                                headers=headers,
                                proxies = {'https':'https://455098435:lbrv3bgb@121.42.140.113:16816'})
        response.encoding = 'utf-8'
        html = response.text
        # with open('./xici.html',mode = 'w',encoding='utf-8') as fp:
        #     fp.write(html)
        result = re.findall(r'<tr.*?>(.*?)</tr>', html, flags=re.S)
        '''<tr class="odd">
      <td class="country"><img src="//fs.xicidaili.com/images/flag/cn.png" alt="Cn"></td>
      <td>182.35.80.136</td>
      <td>9999</td>
      <td>
        <a href="/2019-10-29/shandong">山东泰安</a>
      </td>
      <td class="country">高匿</td>
      <td>HTTP</td>
      <td class="country">
        <div title="0.401秒" class="bar">
          <div class="bar_inner fast" style="width:88%">
            
          </div>
        </div>
      </td>
      <td class="country">
        <div title="0.08秒" class="bar">
          <div class="bar_inner fast" style="width:98%">
            
          </div>
        </div>
      </td>
      
      <td>1分钟</td>
      <td>19-10-29 13:20</td>
    </tr>'''
        print('----------------',len(result))
        for item in result[1:]:
            try:
                ip = re.findall(r'<td>([\d\.]*)</td>', item, re.S)
                type = re.findall(r'<td>([A-Z]+)</td>', item, re.S)
                fp.write('%s,%s,%s\n' % (ip[0], ip[1], type[0]))
            except Exception as e:
                with open('./log.txt',mode = 'a',encoding='utf-8') as f:
                    f.write(item + '\n' + str(e) + '\n')
        print('第%d页代理爬取成功！' % (i))
        time.sleep(random.randint(1, 3))
    fp.close()
num = 0
fp = open('./proxies.txt','r',encoding='utf-8')
fp2 = open('./verified_proxie.txt','a',encoding='utf-8')

def verify_proxy():
    global num
    while True:
        line = fp.readline().strip('\n')
        if line != '':
            try:
                ip,host,protocol = line.split(',')
            except:
                print('------------------------------',line)
            # 要访问的网站，如果是https，那么代理也要是https，不对应不走代理，走本地
            # 要访问的网站，如果是http，那么代理也要是http类型
            url1 = 'http://ip.tool.chinaz.com/'
            url2 = 'https://ip.cn/'
            if protocol == 'HTTPS':
                try:
                    requests.get(url2,proxies = {'https':'%s:%s'%(ip,host)},timeout = 3)
                    print('该ip：%s:%s验证通过'%(ip,host))
                    fp2.write('%s,%s,%s\n'%(ip,host,protocol))
                    num +=1
                except Exception as e:
                    print('该ip：%s:%s验证失败' % (ip, host))
            else:
                try:
                    requests.get(url1, proxies={'http': '%s:%s' % (ip, host)}, timeout=3)
                    print('该ip：%s:%s验证通过' % (ip, host))
                    fp2.write('%s,%s,%s\n' % (ip, host, protocol))
                    num +=1
                except Exception as e:
                    print('该ip：%s:%s验证失败' % (ip, host))
        else:
            break
    return num

if __name__ == '__main__':
    with open('./verified_proxie.txt',mode = 'r',encoding='utf-8') as f:
        proxies = f.readlines()
    proxies = [proxy.strip('\n').split(',') for proxy in proxies]
    print(proxies)
    get_proxies(proxies)
    # threads = []
    # for i in range(1000):
    #     t = threading.Thread(target=verify_proxy)
    #     t.start()
    #     threads.append(t)
    # # join必须单独写，目的：线程启动
    # for t in threads:
    #     t.join()
    # print('-----------------所有的子线程结束任务，主线程开始执行')
    # fp.close()
    # fp2.close()
