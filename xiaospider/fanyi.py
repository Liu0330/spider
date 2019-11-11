# -*- coding: utf-8  -*-
import requests
import json
# import sys

class BaiduFanyi:
    def __init__(self,trans_str):
        self.lang_detect_url ="https: // fanyi.baidu.com / langdetect"
        self.trans_url = "https://fanyi.baidu.com/basetrans"
        self.trans_str = trans_str
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

    def parse_url(self,url,data):
        print(url,data)
        response = requests.post(url,data=data,headers = self.headers)
        # print(response)
        return json.loads(response.content.decode())

    def get_ret(self,dict_response):
        ret = dict_response["trans"][0]["dist"]
        print("result is：",ret)

    def run(self):
        #准备rul地址，post_data
        lang_detect_data = {"query":self.trans_str}
        print(lang_detect_data)
        #发送post请求获取响应

        lang = self.parse_url(self.lang_detect_url,lang_detect_data)["from"]


        trans_data = {"query":self.trans_str,"from":"zh","to":"en"} if lang=="zh"else {"query":self.trans_str,"from":"en","to":"zh"}
        dict_response = self.parse_url(self.trans_url,trans_data)
        self.get_ret(dict_response)




if __name__ == '__main__':
    # trans_str = sys.argv[1]
    baidu_fanyi = BaiduFanyi(trans_str="你好")
    baidu_fanyi.run()