import urllib
from urllib import request
url = 'http://vfx.mtime.cn/Video/2019/10/28/mp4/191028113825939128_480.mp4'
#    "http://vfx.mtime.cn/Video/2019/10/28/mp4/191028 154207354617_480.mp4"
# http://vfx.mtime.cn/Video/2019/10/28/mp4/191028113825939128_480.mp4
if __name__ == '__main__':
    # 高级方法，不需要打开文件，封装好的方法
    print('视频开始下载…………')
    urllib.request.urlretrieve(url = url,filename='./airplane.mp4')
    print('视频保存成功！')