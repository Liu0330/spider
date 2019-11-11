# -*- coding: utf-8 -*-
# @Time    : 2019/05/06 13:46
# @Author  : Liu
# @File    : 02_qiubai_spider.py
import requests
from lxml import etree


class QiubaiSpdier:
    def __init__(self):
        self.url_temp = "https://mp.weixin.qq.com/s/sGrWYWBkGVf3llo1Bcv_Ug"
        self.headers = {"User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}

    def parse_url(self, url):
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode()

    def get_content_list(self, html_str):  # 提取数据
        html = etree.HTML(html_str)
        div_list = html.xpath("//div[@id='content-left']/div/.//div[@class='content']/span/text()")  # 分组//*[@id="content-left"]

    def run(self):  # 实现主要逻辑
        # 1.url_list
        url_list = self.get_url_list()

if __name__ == '__main__':
    qiubai = QiubaiSpdier()
    qiubai.run()