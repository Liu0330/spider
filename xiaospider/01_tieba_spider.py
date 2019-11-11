# coding=utf-8
import requests
from lxml import etree
import json

class TiebaSpider:
    def __init__(self,tieba_name):
        self.tieba_name = tieba_name
        self.start_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/m?kw="+tieba_name+"&pn=0"
        self.part_url = "http://tieba.baidu.com/mo/q----,sz@320_240-1-3---2/"
        self.headers= {"User-Agent":"Mozilla/5.0 (Linux; Android 5.1.1; Nexus 6 Build/LYZ28E) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Mobile Safari/537.36"}
    def parse_url(self,url):#发送请求，获取响应
        print(url)
        response = requests.get(url,headers=self.headers)
        return response.content

    def get_content_list(self,html_str):#3提取数据
        html = etree.HTML(html_str)

        div_list = html.xpath("//div[contains(@class,'i')]") #根据div分组
        content_list = []
        for div in div_list:
            item = {}
            item["title"] = div.xpath("./a/text()")[0] if len(div.xpath("./a/text()"))>0 else None
            item["href"] = self.part_url+div.xpath("./a/@href")[0] if len(div.xpath("./a/@href"))>0 else None
            item["img_list"] = self.get_img_list(item["href"],[])
            # itemp["img_list"] = [requests.utils.unquote(i).split("src=")[-1] for i in item["img_list"]]
            content_list.append(item)
        #提取下一页的url地址
        next_url = self.part_url+html.xpath("//a[text()='下一页']/@href")[0] if len(html.xpath("//a[text()='下一页']/@href"))>0 else None
        return content_list,next_url

    def get_img_list(self,detail_url,total_img_list): #获取帖子中的所有的图片
        #3.2请求列表页的url地址，获取详情页的第一页
        detail_html_str = self.parse_url(detail_url)
        detail_html = etree.HTML(detail_html_str)
        #3.3提取详情页第一页的图片，提取下一页的地址
        img_list = detail_html.xpath("//img[@class='BDE_Image']/@src")
        total_img_list.extend(img_list)
        #3.4请求详情页下一页的地址，进入循环3.2-3.4
        detail_next_url = detail_html.xpath("//a[text()='下一页']/@href")
        if len(detail_next_url)>0:
            detail_next_url =  self.part_url + detail_next_url[0]
            return self.get_img_list(detail_next_url,total_img_list)
        # else:
        #     return total_img_list
        return total_img_list

    def save_content_list(self,content_list): #4保存数据
        file_path = self.tieba_name+".txt"
        with open(file_path,"a",encoding="utf-8") as f:
            for content in content_list:
                f.write(json.dumps(content,ensure_ascii=False,indent=2))
                f.write("\n")
        print("保存成功")

    def run(self):#实现主要逻辑
        next_url = self.start_url
        while next_url is not None:
            #1.start_url
            #2.发送请求，获取响应
            html_str = self.parse_url(next_url)
            #3.提取数据，提取下一页的url地址
                #3.1提取列表页的url地址和标题
                #3.2请求列表页的url地址，获取详情页的第一页
                #3.3提取详情页第一页的图片，提取下一页的地址
                #3.4请求详情页下一页的地址，进入循环3.2-3.4
            content_list,next_url = self.get_content_list(html_str)
            #4.保存数据
            self.save_content_list(content_list)
            #5.请求下一页的url地址，进入循环2-5·

if __name__ == '__main__':
    tieba_spider = TiebaSpider("冷清清")
    tieba_spider.run()
