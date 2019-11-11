import requests
from lxml import etree
url1 = 'https://www.neihanba.com/dz/'
url = 'https://www.neihanba.com/dz/list_%d.html'
if __name__ == '__main__':
    fp = open('./duanzi.csv',mode = 'a',encoding='utf-8')
    for i in range(1,101):
        if i == 1:
            url_duanzi = url1
        else:
            url_duanzi = url%(i)
        response = requests.get(url_duanzi)
        response.encoding = 'gbk'
        content = response.text
        html = etree.HTML(content)
        result = html.xpath('//ul[@class="piclist longList"]/li')
        for li in result:
            try:
                title = li.xpath('.//h4/a/b/text()')[0]
                content = li.xpath('.//div[@class="f18 mb20"]/text()')[0].strip().strip('\n')
                info = ''.join(li.xpath('.//div[@class="ft"]/span//text()')[1:])
                fp.write('%s\t%s\t%s\n'%(title,content,info))
            except Exception as e:
                # 异常保存，第二天，分析，单独爬取。
                pass
        print('第%d页内容保存成功！'%(i))
    fp.close()
    # ！！！缺少异常捕获