import requests
import time

url = ['http://bbs.mobiletrain.org/forum.php?mod=viewthread&tid=1103024&extra=page%3D1%26filter%3Dtypeid%26typeid%3D1364',
       'http://bbs.mobiletrain.org/forum.php?mod=viewthread&tid=1103024&extra=page%3D1%26filter%3Dtypeid%26typeid%3D1364']

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36'}

count = 0
countUrl = len(url)

# 访问次数设置
while count < 725:
    try:  # 正常运行
        for i in range(countUrl):
            response = requests.get(url[i], headers=headers)
            if response.status_code == 200:
                count = count + 1
                print('Success ' + str(count), 'times')
        time.sleep(0)

    except Exception:  # 异常
        print('Failed and Retry')
        time.sleep(0)
