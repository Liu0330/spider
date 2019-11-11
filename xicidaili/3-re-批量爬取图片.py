import requests
import re
url1 = 'http://sc.chinaz.com/tupian/index.html'
url = 'http://sc.chinaz.com/tupian/index_%d.html'
num = 0
def download_images(img_urls):
    global num
    for img_url in img_urls:
        response = requests.get(img_url)
        filename = img_url.rsplit('/',1)[-1]
        with open('./pictures/%s'%(filename),mode = 'wb') as fp:
            fp.write(response.content)
            print('------------图片：%s保存成功-----------'%(filename))
            num += 1
    return num

if __name__ == '__main__':
    # response = requests.get(url1)
    # response.encoding = 'utf-8'
    # with open('./picture.html',mode='w',encoding='utf-8') as fp:
    #     fp.write(response.text)
    #     print('------------数据保存成功')
    for i in range(1,11):
        if i == 1:
            url_pic = url1
        else:
            url_pic = url%(i)
        response = requests.get(url_pic)
        response.encoding = 'utf-8'
        content = response.text
        '''<img src2="http://pic2.sc.chinaz.com/Files/pic/pic9/201910/bpic14126_s.jpg"'''
        img_urls = re.findall(r'<img src2="(.*?)"',content)
        # 单独下载图片的方法
        number = download_images(img_urls)
    print('共计下载图片多少张%d'%(number))
