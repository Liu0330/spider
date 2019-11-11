import time

import requests
from selenium import webdriver

url ='https://sou.zhaopin.com/?jl=530&kw=python&kt=3'
if __name__ == '__main__':


    headers={
'accept':' text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
# 'accept-encoding':' gzip, deflate, br',
'accept-language':' zh-CN,zh;q=0.9',
'cache-control':' max-age=0',
'cookie: sts_deviceid=16e1fbed7eb17e-018f331400043c-51402e1a-1327104-16e1fbed7ec3b6; x-zp-client-id=09a3635c-5e1b-4dc7-f9e8-f14174e143c0; urlfrom=121114583; urlfrom2=121114583; adfcid=www.baidu.com; adfcid2=www.baidu.com; adfbid=0; adfbid2=0; sajssdk_2015_cross_new_user=1; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216e1fbedab5fc-01739481051842-51402e1a-1327104-16e1fbedab6577%22%2C%22%24device_id%22%3A%2216e1fbedab5fc-01739481051842-51402e1a-1327104-16e1fbedab6577%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E8%87%AA%E7%84%B6%E6%90%9C%E7%B4%A2%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.baidu.com%2Flink%22%7D%7D; sts_sg=1; sts_sid=16e1fbedad52d7-0475863d124be1-51402e1a-1327104-16e1fbedad650d; sts_chnlsid=Unknown; zp_src_url=https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DdqpadXJU-Hhsn0IFw5XDW5CKUeP4An6i-l2_u1BRuyu%26wd%3D%26eqid%3De5ae1c3e0001bc96000000025dba4d84; dywea=95841923.3569941739922393600.1572490632.1572490632.1572490632.1; dywec=95841923; dywez=95841923.1572490632.1.1.dywecsr=baidu|dyweccn=(organic)|dywecmd=organic; __utma=269921210.979477302.1572490632.1572490632.1572490632.1; __utmc=269921210; __utmz=269921210.1572490632.1.1.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmt=1; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1572490632; jobRiskWarning=true; dyweb=95841923.2.10.1572490632; __utmb=269921210.2.10.1572490632; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; acw_tc=3ccdc15c15724906810542726e179639a2142bf7f097cd6331c5371fbbe1c8; acw_sc__v3=5dba4dbaeb3d7ebbfeb1827d50f618a1c48f4060; acw_sc__v2=5dba4db9c4aa80c1e4ea55899f48a91e4bd6bd2e; sou_experiment=capi; ZP_OLD_FLAG=false; POSSPORTLOGIN=9; CANCELALL=0; ZL_REPORT_GLOBAL={%22//www%22:{%22seid%22:%22%22%2C%22actionid%22:%22de147ff6-d74a-4600-bd50-2376b8978733-cityPage%22}%2C%22sou%22:{%22actionid%22:%22850a74f3-8314-4230-a679-1c00f6e9ded9-sou%22%2C%22funczone%22':'%22smart_matching%22}}; sts_evtseq=13; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1572490706',
'referer: https':'//sou.zhaopin.com/?jl=530&kw=python&kt=3&',
'sec-fetch-mode':' navigate',
'sec-fetch-site':' same-origin',
'sec-fetch-user':' ?1',
'upgrade-insecure-requests':' 1',
'user-agent':' Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',

    }
    url ='https://sou.zhaopin.com/?jl=530&kw=python&kt=3'
    response = requests.get(url,headers)
    response.encoding='gbk'
    print(response.text)

    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(url)
    time.sleep(5)
    driver.find_element_by_xpath('//div[@class='']/button')
    with open('./zhilian.html','wb',encoding='utf-8')as fp:
        fp.write(driver.page_source)
        driver.close()


