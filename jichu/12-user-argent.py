# -*- coding: utf-8 -*-

# https://shortvideo.mtime.cn/play/getPlayUrl?videoId=76637&scheme=http&source=1



import requests

url = 'https://www.alibabacloud.com/'

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'ja',
    'cache-control': 'max-age=0',
    # 'cookie': 'rmStore=amid:43301; cna=rmYyEsEd30cCAXEsPzFWoeTj; _ga=GA1.2.1367703733.1568792216; _bl_uid=6kkdt0q8yC4oR7f8sua1ssdn79j1; _gcl_au=1.1.16888860.1572066579; _a1_f=05446644-4647-48a2-97b8-ba005837974e; _a1_u=cc112ed6-0ddd-4fcc-9fb3-e15244ae9d7a; aliyun_intl_choice=intl; aliyun_choice=intl; channel=dKsTees6Al%2BEiEMRvDS1%2B1mTbasaRX6c5te2hkguUs4%3D; JSESSIONID=2S566MC1-PXN9AL095E4M4CTO03CV3-ZM138A2K-CMEB; tmp0=xVgIN3LPTxSEseclRSibqGhVnvM4S2n3tfsJB5Q4Vi1U%2FSSMxtfurGyJXajn6OOtJevTE4ZjC0n6KVQEDIg7RBU89saBYwxbFZ2CLfvmzrHg0IKQ2uSh06n%2Fb57Qfyq1RMo9rqjpmWVwHFkKhtS8kA%3D%3D; _gid=GA1.2.420087605.1572255091; aliyun_lang=fr; stc115239=env:1572255089%7C20191128093129%7C20191028100201%7C4%7C1047918:20201027093201|uid:1568792216181.1636209792.1378274.115239.351290079.:20201027093201|srchist:1047918%3A1572255089%3A20191128093129:20201027093201|tsa:-771316086:20191028100201; login_aliyunid_csrf=_csrf_tk_1290372255120177; isg=BPDwLQNmWUUTnAV2RKleQLPMwb5COdSD9s0_FupBqMsepZBPkkqMEkOX-e1gA4xb',
    'referer': 'https://www.alibabacloud.com/ja',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36', }
if __name__ == '__main__':
    response = requests.get(url=url,headers = headers)
    print(response.text)
    'ffmpeg -i 2-背景介绍.mp4 -vcodec copy -acodec copy -vbsf h264_mp4toannexb 1.ts'