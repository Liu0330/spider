# coding=utf-8

import requests
import json


class BaiDuTranslatePhone:
    def __init__(self):
        self.query = input("请输入要翻译的内容：")
        self.url = "https://fanyi.baidu.com/basetrans"
        self.data = {
            "query": self.query,
            "from": "zh",
            "to": "en"
        }
        self.headers = {
            "Host": "fanyi.baidu.com",
            "User-Agent": "xxx",
            "Referer": "https://fanyi.baidu.com/?aldtype=16047"
        }

    def run(self):
        post_response = requests.post(url=self.url, data=self.data, headers=self.headers)
        self.strs = post_response.content.decode()
        # print(self.strs)
        # print("self.strs type:"+str(type(self.strs)))

    def get_result(self):
        result_dict = json.loads(self.strs)
        # print("result_dict type:"+str(type(result_dict)))
        result = result_dict['trans'][0]['dst'] if len(result_dict['trans']) > 0 else None
        print("翻译结果为：")
        print(result)


if __name__ == '__main__':
    while True:
        translate = BaiDuTranslatePhone()
        translate.run()
        translate.get_result()