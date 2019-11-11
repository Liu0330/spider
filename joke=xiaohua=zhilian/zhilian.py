import urllib

import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
url = 'https://www.zhaopin.com/'
headers = {'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
# 'accept-encoding':'gzip, deflate, br',
'accept-language':'zh-CN,zh;q=0.9',
'cache-control':'max-age=0',
'cookie':'dywem=95841923.y; NTKF_T2D_CLIENTID=guest2017FE6E-3694-7339-7A82-58AEDD55E252; adfbid2=0; __utmv=269921210.|2=Member=1912450118=1; sts_deviceid=1644ade919f62b-0c98b56ecbd29b-3961430f-1327104-1644ade91a06aa; _qzja=1.546852014.1513168714274.1529891891874.1531819410886.1531819667714.1531819684319.0.0.0.212.41; urlfrom2=121113803; _jzqa=1.1653535386403270000.1508291900.1552958878.1553160388.67; __xsptplus30=30.72.1553160387.1553160387.1%232%7Csp0.baidu.com%7C%7C%7C%25E6%2599%25BA%25E8%2581%2594%25E6%258B%259B%25E8%2581%2598%7C%23%23n9Js8IAuS3VhJNqVx9lrHq3su7f3RsY7%23; x-zp-client-id=a4b4bda0-6b3b-463c-bb10-bfe126e7198d; registerGroup=psapi; sou_experiment=psapi; ZP_OLD_FLAG=false; acw_tc=3ccdc15b15722296959246859e6169ed69db8cc59d5df2ce7c4dbb42ce03d0; urlfrom=121113803; adfbid=0; sts_sg=1; sts_sid=16e1fbe4536380-0a8c23770ab81c-7711439-629760-16e1fbe45375bb; sts_chnlsid=121113803; zp_src_url=https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0jZ7-0KqiAsKIHUGI00000P_OfNC00000LCDJiZ.THLyktAJ0A3qmh7GuZNCUvd-gLKM0ZnqrH63uhRzmhnsnj0kPHbzmsKd5HK7nD7AwjmdwHm1PWIaPHI7wRRdPHR3nbuafW61f10Y0ADqI1YhUyPGujY1nW63rHb3nWbdFMKzUvwGujYkP6K-5y9YIZK1rBtEILILQMGCmyqspy38mvqV5LPGujYknWDknHn3njnhIgwVgLPEIgFWuHdBmy-bIgKWTZChIgwVgvd-uA-dUHdWTZf0mLFW5HTLnf%26tpl%3Dtpl_11534_19968_16032%26l%3D1514225627%26attach%3Dlocation%253D%2526linkName%253D%2525E6%2525A0%252587%2525E5%252587%252586%2525E5%2525A4%2525B4%2525E9%252583%2525A8-%2525E6%2525A0%252587%2525E9%2525A2%252598-%2525E4%2525B8%2525BB%2525E6%2525A0%252587%2525E9%2525A2%252598%2526linkText%253D%2525E3%252580%252590%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525E3%252580%252591%2525E5%2525AE%252598%2525E6%252596%2525B9%2525E7%2525BD%252591%2525E7%2525AB%252599%252520%2525E2%252580%252593%252520%2525E5%2525A5%2525BD%2525E5%2525B7%2525A5%2525E4%2525BD%25259C%2525EF%2525BC%25258C%2525E4%2525B8%25258A%2525E6%252599%2525BA%2525E8%252581%252594%2525E6%25258B%25259B%2525E8%252581%252598%2525EF%2525BC%252581%2526xp%253Did(%252522m3288998295_canvas%252522)%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FDIV%25255B1%25255D%25252FH2%25255B1%25255D%25252FA%25255B1%25255D%2526linkType%253D%2526checksum%253D64%26wd%3D%25E6%2599%25BA%25E8%2581%2594%26issp%3D1%26f%3D8%26ie%3Dutf-8%26rqlang%3Dcn%26tn%3Dbaiduhome_pg%26inputT%3D1606; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22637483372%22%2C%22%24device_id%22%3A%22166afb9e5444d6-04ec298b2a3bf7-5e442e19-1327104-166afb9e54649c%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E4%BB%98%E8%B4%B9%E5%B9%BF%E5%91%8A%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fsp0.baidu.com%2F9q9JcDHa2gU2pMbgoY3K%2Fadrc.php%3Ft%3D06KL00c00fZmx9C0jZ7-0KqiAsKIHUGI00000P_OfNC00000LCDJiZ.THLyktAJ0A3qmh7GuZNCUvd-gLKM0ZnqrH63uhRzmhnsnj0kPHbzmsKd5HK7nD7AwjmdwHm1PWIaPHI7wRRdPHR3nbu%22%2C%22%24latest_search_keyword%22%3A%22%E6%99%BA%E8%81%94%22%2C%22%24latest_utm_source%22%3A%22baidupcpz%22%2C%22%24latest_utm_medium%22%3A%22cpt%22%2C%22%24latest_utm_campaign%22%3A%22pp%22%2C%22%24latest_utm_content%22%3A%22sjz%22%2C%22%24latest_utm_term%22%3A%2225250256%22%7D%2C%22first_id%22%3A%22166afb9e5444d6-04ec298b2a3bf7-5e442e19-1327104-166afb9e54649c%22%7D; rt=1159f77a41c04b9cab87a81ce309ab01; at=2d46883c5e8b4f4fa362173d3ecf5857; dywea=95841923.2099730433246266600.1508291895.1572233535.1572490668.113; dywec=95841923; dywez=95841923.1572490668.113.86.dywecsr=landing.zhaopin.com|dyweccn=(referral)|dywecmd=referral|dywectr=undefined|dywecct=/register; dyweb=95841923.1.10.1572490668; jobRiskWarning=true; __utma=269921210.1428116669.1508291899.1572233535.1572490669.118; __utmc=269921210; __utmz=269921210.1572490669.118.84.utmcsr=landing.zhaopin.com|utmccn=(referral)|utmcmd=referral|utmcct=/register; __utmt=1; __utmb=269921210.1.10.1572490669; Hm_lvt_38ba284938d5eddca645bb5e02a02006=1571883579,1572229687,1572361072,1572490669; LastCity=%E5%8C%97%E4%BA%AC; LastCity%5Fid=530; privacyUpdateVersion=2; acw_sc__v2=5dba4db1e873f6a7aea2c5ae93b0c19c12c766c8; POSSPORTLOGIN=4; CANCELALL=0; Hm_lpvt_38ba284938d5eddca645bb5e02a02006=1572490677; ZL_REPORT_GLOBAL={%22sou%22:{%22actionid%22:%22d34d06ec-8693-4610-9688-61d0a5cc2462-sou%22%2C%22funczone%22:%22smart_matching%22}}; sts_evtseq=9',
'referer':'https://sou.zhaopin.com/?jl=530&kw=python&kt=3&sf=0&st=0',
'sec-fetch-mode':'navigate',
'sec-fetch-site':'same-origin',
'sec-fetch-user':'?1',
'upgrade-insecure-requests':'1',
'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36',}
'''https://fe-api.zhaopin.com/c/i/sou?pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&=0&at=2d46883c5e8b4f4fa362173d3ecf5857&rt=1159f77a41c04b9cab87a81ce309ab01&_v=0.79710597&userCode=637483372&x-zp-page-request-id=582ec2a565904b85b9017a64860cdbad-1572491095565-275414&x-zp-client-id=a4b4bda0-6b3b-463c-bb10-bfe126e7198d'''
'''https://fe-api.zhaopin.com/c/i/sou?start=180&pageSize=90&cityId=530&salary=0,0&workExperience=-1&education=-1&companyType=-1&employmentType=-1&jobWelfareTag=-1&kw=python&kt=3&=0&at=2d46883c5e8b4f4fa362173d3ecf5857&rt=1159f77a41c04b9cab87a81ce309ab01&_v=0.79710597&userCode=637483372&x-zp-page-request-id=582ec2a565904b85b9017a64860cdbad-1572491095565-275414&x-zp-client-id=a4b4bda0-6b3b-463c-bb10-bfe126e7198d'''


def get_page_mes():
    global jobs, job, title, hrefxpath, href, e
    time.sleep(5)
    jobs = driver.find_elements_by_xpath('//div[@id="listContent"]/div')
    for job in jobs:
        try:
            title = job.find_element_by_xpath('.//span').get_attribute("title")
            print(title)

            hrefxpath = './div//a'
            href = job.find_element_by_xpath(hrefxpath).get_attribute("href")
            print(href)
        except Exception as e:
            print(e)
            break
next_flag= True

if __name__ == '__main__':
    # response = requests.get(url = url,headers = headers)
    # response.encoding = 'utf-8'
    # print(response.text)
    # 初始化
    driver = webdriver.Chrome()
    driver.implicitly_wait(5)
    driver.get(url)

    #关闭data再回来
    windows = driver.window_handles
    driver._switch_to.window(windows[1])
    driver.close()
    windows = driver.window_handles
    driver._switch_to.window(windows[0])

    #关闭弹窗
    driver.find_element_by_xpath('//div[@class="risk-warning__content"]/button').click()
    #输入python
    driver.find_element_by_xpath('//div[@class="zp-search__common"]//input').send_keys("python")
    #点击搜索
    driver.find_element_by_xpath('//a[@class="zp-search__btn zp-search__btn--blue"]').click()
    #切换窗口
    windows = driver.window_handles
    # print(windows)
    driver._switch_to.window(windows[1])
    #点击城市
    driver.find_element_by_xpath('//li[@class="currentCity query-city__uls__li current-city"]').click()
    # 点击北京
    driver.find_element_by_xpath('//li[@class="cityItemBox city-child__choise__city"]/a').click()

    #保存文件
    # with open('./zhilian.html','w',encoding='utf-8') as fp:
    #     fp.write(driver.page_source)
    #     print('页面的数据获取成功')

    #获取当前页面Jobs
    get_page_mes()

    # button_next ='/html/body/div[1]/div[1]/div[4]/div[3]/div[3]/div/div[91]/div/div/div/button[2]'
    #如果有下一页 next_flag默认为T
    while next_flag:
        try:
            time.sleep(5)
            next = driver.find_element_by_xpath('//button[@class="btn soupager__btn"]')
            print('获取到下一页元素',next)
            try:
                next.send_keys(Keys.ENTER)
            except Exception as e:
                print("点击错误", e)
        except Exception as e:
            print("没有获得下一页",e)
            next_flag = False
            break

        get_page_mes()


