# coding=utf-8
import requests

class TiebaSpider:
    def __init__(self,tieba_name):
        self.url_temp = "https://tieba.baidu.com/f?kw="+tieba_name+"&ie=utf-8&pn={}"
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}
        self.tieba_name = tieba_name

    def get_url_list(self):
        # ur_list = []
        # for i in range(1000):
        #     ur_list.append(self.url_temp.format(i*50))
        # return ur_list
        # print([self.url_temp.format(i * 50) for i in range(1000)])
        return [self.url_temp.format(i*50) for i in range(1000)]



    def parse_url(self,url):
        response = requests.get(url,headers = self.headers)
        return response.content

    def save_html(self,html_str,page_num ):
        file_path = "{}--第{}页.html".format(self.tieba_name,page_num)
        with open(file_path,"wb+") as f :
            f.write(html_str)
            print(file_path)

    def run(self): #实现主要逻辑
        #1.url列表构造
        ur_list = self.get_url_list()
        #2.遍历发送请求，获取响应
        for url in ur_list:
            html_str = self.parse_url(url)
        #3.保存
            page_num = ur_list.index(url)+1
            self.save_html(html_str,page_num)

if __name__ == '__main__':
    tieba_spider = TiebaSpider("李毅")
    tieba_spider.run()