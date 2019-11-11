import re
import requests
import threading
url1 = 'http://sc.chinaz.com/tupian/index.html'
url = 'http://sc.chinaz.com/tupian/index_%d.html'

# 作业，线程池，优化
def download_image(img_url):
    response = requests.get(img_url)
    filename = img_url.rsplit('/',1)[-1]
    with open('./pictures/%s'%(filename),mode = 'wb') as fp:
        fp.write(response.content)
        print('-------图片%s保存成功--------'%(filename))
def get_image_urls(num):
    for i in range(1,num + 1):
        if i == 1:
            url_pic = url1
        else:
            url_pic = url%(i)
        print('-------开始下载第%d页图片--------'%(i))
        response = requests.get(url_pic)
        response.encoding = 'utf-8'
        img_urls = re.findall(r'<img src2="(.*?)"', response.text)
        for img_url in img_urls:
            t = threading.Thread(target = download_image,args = (img_url,))
            t.start()
if __name__ == '__main__':
    try:
        num = int(input('请输入获取的页码数量：'))
    except:
        print('请输入数字！')
        num = int(input('请输入获取的页码数量：'))
    get_image_urls(num)