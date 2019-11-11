headpools = [
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
    'Opera/8.0 (Windows NT 5.1; U; en)',
    'Mozilla/5.0 (Windows NT 5.1; U; en; rv:1.8.1) Gecko/20061208 Firefox/2.0.0 Opera 9.50',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:34.0) Gecko/20100101 Firefox/34.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.57.2 (KHTML, like Gecko) Version/5.1.7 Safari/534.57.2',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.71 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; QQBrowser/7.0.3698.400)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.84 Safari/535.11 SE 2.X MetaSr 1.0',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Maxthon/4.4.3.4000 Chrome/30.0.1599.101 Safari/537.36'
]
import urllib.request, re, random


def ua():
    a = random.choice(headpools)
    user_agen = ('User-Agent', a)
    ua_1 = urllib.request.build_opener()
    ua_1.add_handlers = [user_agen]
    urllib.request.install_opener(ua_1)


for i in range(3):
    code = input('请输入起点小说编码：')
    d = input('下载章节数：')
    while True:
        try:
            d = int(d)
            break
        except:
            d = input('请输入正确下载章节数量：')
    dir = input('文件保存路径：').replace('\\', r'\\') + r'\\'
    ua()
    path = ',"cU":"(.*?)"'
    data = urllib.request.urlopen(
        'https://read.qidian.com/ajax/book/category?_csrfToken=W3Qw76uPjNrWkGswLpkjV5faKrFYI84CMGrLiRmu&bookId=' + code).read().decode(
        'utf-8', 'ignore')
    screen = re.compile(path).findall(data)  # 筛选各个章节的网址乱码

    for i in range(d):  # 循环次数，及第0-X章节
        data_1 = urllib.request.urlopen('https://read.qidian.com/chapter/' + screen[i]).read().decode('utf-8', 'ignore')
        path_1 = '<div class="read-content j_readContent">(.*?)</div>'
        screen_1 = re.compile(path_1, re.S).findall(data_1)  # 正文一筛选
        path_2 = '<p>\u3000\u3000'
        screen_2 = re.sub(path_2, '\n\n', screen_1[0])  # 正文二筛选
        path_name = 'rName">(.*?)</h3>'
        name = re.compile(path_name).findall(data_1)  # 章节名筛选
        file = open(dir + name[0] + '.txt', 'w')
        file.write(name[0] + screen_2)
        file.close()
        print('下载完成：' + name[0])