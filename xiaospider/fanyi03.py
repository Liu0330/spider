# -*- coding: utf-8  -*-
import requests
import execjs
import json


class BaiDuTranslateWeb:
    def __init__(self):
        self.url = "https://fanyi.baidu.com/v2transapi"
        self.headers = {
            "Cookie": "BAIDUID=CFEE9080DF6E776E0123848EB77FC60B:FG=1; BIDUPSID=CFEE9080DF6E776E0123848EB77FC60B; PSTM=1555988123; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; BDUSS=FFaHZpbnJ1U1gwNU9TeGtuSkZudlZKfmtaNHdrbHpBZkkxbDI4OEZkSzhjT3BjRVFBQUFBJCQAAAAAAAAAAAEAAAAD74Bo2drR~jIwMTUAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAALzjwly848JcWT; from_lang_often=%5B%7B%22value%22%3A%22it%22%2C%22text%22%3A%22%u610F%u5927%u5229%u8BED%22%7D%2C%7B%22value%22%3A%22fra%22%2C%22text%22%3A%22%u6CD5%u8BED%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; H_PS_PSSID=1447_21126_28774_28722_28964_28831_28584_26350; delPer=0; PSINO=2; locale=zh; Hm_lvt_afd111fa62852d1f37001d1f980b6800=1556933493,1556935638; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1556933482,1556933493,1556935629,1556935638; Hm_lpvt_afd111fa62852d1f37001d1f980b6800=1556935645; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1556935645",
            "User-Agent":  "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36",
        }
        self.data = {
            "from": "zh",
            "to": "en",
            "query": None,
            "transtype": "translang",
            "simple_means_flag": 3,
            "sign": None,
            "token": "300f465c88543c5218f056447a33a348"
        }

    def get_baidu_sign(self):
        with open("baidusign.js") as f:
            jsData = f.read()
            sign = execjs.compile(jsData).call("e", self.input)
            return sign

    def run(self):
        self.input = input("请输入要翻译的内容：")
        self.get_baidu_sign()
        self.data["query"] = self.input
        self.data["sign"] = self.get_baidu_sign()
        response = requests.post(url=self.url, data=self.data, headers=self.headers)
        self.result_strs = response.content.decode()

    def get_translate_result(self):
        result_dict = json.loads(self.result_strs)
        if 'trans_result' in result_dict:
            result_dict = result_dict['trans_result']['data'][0] if len(
                result_dict['trans_result']['data']) > 0 else None
            result_dict = result_dict['result'][0] if len(result_dict['result']) > 0 else None
            result = result_dict[1] if len(result_dict) > 1 else None
            print("翻译结果为：")
            print(result)
        else:
            print("请输入内容再进行翻译")


if __name__ == '__main__':
    while True:
        baidutranlate = BaiDuTranslateWeb()
        baidutranlate.run()
        baidutranlate.get_translate_result()