# coding=utf-8
import requests,re,json
from lxml import etree

class QiubaiSpdier:
    def __init__(self):
        self.url_temp = "https://m.weibo.cn/api/container/getIndex?type=uid&value=3267187212&containerid=1076033267187212&since_id=4360257751302636"
        self.headers = {"User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1"}
    def get_url_list(self):
        return [self.url_temp.format(i) for i in range(1,14)]

    def parse_url(self,url):
        print(url)
        response = requests.get(url,headers=self.headers)
        return response.content.decode('raw_unicode_escape')

    def get_content_list(self,html_str): #提取数据
        html = etree.HTML(html_str)
        div_list = html.xpath("raw_text")  #分组

        # print(html)
        content_list = []
        for div in div_list:
            item= {}
            item["content"] = div.xpath("//div[@class='weibo-text']/text()")
            # item["content"] = [i.replace("\n","") for i in item["content"]]
            # item["author_gender"] = div.xpath("//div[@class='m-container-max']")
            # item["author_gender"] = item["author_gender"][0].split(" ")[-1].replace("Icon","") if len(item["author_gender"])>0 else None
            # item["auhtor_age"] = div.xpath(".//div[contains(@class,'articleGender')]/text()")
            # item["auhtor_age"] = item["auhtor_age"][0] if len(item["auhtor_age"])>0 else None
            # item["content_img"] = div.xpath(".//div[@class='thumb']/a/img/@src")
            # item["content_img"] = "https:"+item["content_img"][0] if len(item["content_img"])>0 else None
            # item["author_img"] = div.xpath(".//div[@class='author clearfix']//img/@src")
            # item["author_img"] = "https:"+item["author_img"][0] if len(item["author_img"])>0 else None
            # item["stats_vote"] = div.xpath(".//span[@class='stats-vote']/i/text()")
            # item["stats_vote"] = item["stats_vote"][0] if len(item["stats_vote"])>0 else None
            content_list.append(item)
        return content_list

    def save_content_list(self,html_str): #保存
        with open("weibo1.txt","a",encoding="gbk") as f:
            for content in html_str:
                f.write(json.dumps(content,ensure_ascii=False))
                f.write("\n")
        print("保存成功")

    def run(self): #实现主要逻辑
        #1.url_list
        url_list = self.get_url_list()
        #2.遍历，发送请求，获取响应
        for url in url_list:
            html_str = self.parse_url(url)

            #3.提取数据
            content_list = self.get_content_list(html_str)
            #4.保存
            self.save_content_list(content_list)

if __name__ == '__main__':
    qiubai = QiubaiSpdier()
    qiubai.run()