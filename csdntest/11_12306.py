# # -*- coding: utf-8 -*-
# # @Time    : 2019/07/15 20:43
# # @Author  : Liu
# # @File    : 11_12306.py
# import requests
# import base64
# import re
#
#
# def get_point(index):
#     map = {
#         '1': '37,46',
#         '2': '110,46',
#         '3': '181,46',
#         '4': '253,46',
#         '5': '37,116',
#         '6': '110,116',
#         '7': '181,116',
#         '8': '253,116',
#     }
#     index = index.split(',')
#     temp = []
#     for item in index:
#         temp.append(map[item])
#     return ','.join(temp)
#
#
# # 实例化一个Session
# session = requests.Session()  # 自动的处理cookie
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
# }
# session.headers.update(headers)
#
# # 伪装成浏览器
# # 1. 访问 获取cookie
# cookie_url = 'https://kyfw.12306.cn/otn/login/conf'
# response = session.get(cookie_url)
# # 2. 下载验证码
# captcha_url = 'https://kyfw.12306.cn/passport/captcha/captcha-image64?login_site=E&module=login&rand=sjrand&1541686714134&callback=jQuery19109992892609908492_1541686371355&_=1541686371356'
# response = session.get(captcha_url)
# data = response.text
# img_base64 = re.findall(r'"image":"(.*?)"', data)[0]
# # img_base64 = 'data:image/jpg;base64,' + img_base64
# # 转换成二级制数据
# img_bytes = base64.b64decode(img_base64)
# # 写到文件
# with open('captcha.jpg', 'wb') as f:
#     f.write(img_bytes)
#
# # 3校验验证码
# check_captcha = 'https://kyfw.12306.cn/passport/captcha/captcha-check?callback=jQuery19109992892609908492_1541686371355&rand=sjrand&login_site=E&_=1541686371358'
# response = session.get(check_captcha, params={
#     'answer': get_point(input('请输入正确的序号>>>:'))})  # 验证码输入，请输入正确验证码的序号（不是坐标），序号之间以,号隔开，验证码在程序目录下
# res = response.text
# code = re.findall(r'"result_code":"(.*?)"', res)[0]
# if code == '4':
#     print('验证码校验成功')
#     # 4 校验用户名密码
#     login_url = 'https://kyfw.12306.cn/passport/web/login'
#     form_data = {
#         'username': '18332191389',  # 替换成自己的12306账号
#         'password': 'l1314521w',  # 替换成自己的12306密码
#         'appid': 'otn'
#     }
#     response = session.post(login_url, data=form_data)
#     res = response.json()
#     if res["result_code"] == 0:
#         print('用户名密码校验成功！')
#         # 5获取权限token
#         uamtk_url = 'https://kyfw.12306.cn/passport/web/auth/uamtk'
#         response = session.post(uamtk_url, data={'appid': 'otn'})
#         res = response.json()
#         if res["result_code"] == 0:
#             print('获取token成功')
#             # 6.校验 token
#             check_token_url = 'https://kyfw.12306.cn/otn/uamauthclient'
#             response = session.post(check_token_url, data={'tk': res['newapptk']})
#             print(response.text)

import json
import requests
import urllib3
import os
import pickle
import re

FILENAME = 'station.pickle'

urllib3.disable_warnings()
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
    "Host": "kyfw.12306.cn",
    "Referer": "https://kyfw.12306.cn/otn/passport?redirect=/otn/"
}

SESSION = requests.Session()
SESSION.headers.update(HEADERS)
SESSION.verify = False
SESSION.get('https://kyfw.12306.cn/otn/login/init')


def station_name():
    url = 'https://kyfw.12306.cn/otn/resources/js/framework/station_name.js?station_version=1.9085'
    response = SESSION.get(url)
    station_name = {}

    station_list = response.text.replace('var station_names =', '')
    station_list = station_list[1:-2]
    station_list = station_list.split('@')[1:]

    for i in station_list:
        i = i.split('|')
        station_name[i[1]] = i[2]

    with open(FILENAME, 'wb') as f:
        pickle.dump(station_name, f)


def check_ticket():
    from_station_name = input('请输入你的出发地（例如：北京）：\n')
    to_station_name = input('请输入你的目的地（例如：上海）：\n')
    date = input('请输入你的乘车时间（例如：2018-12-27）：\n')
    with open(FILENAME, 'rb') as f:
        station_name = pickle.load(f)

    try:
        from_station_code = station_name[from_station_name]
        to_station_code = station_name[to_station_name]
        date_re = re.search(r"\d{4}-\d{1,2}-\d{1,2}", date)
        if date_re == None:
            print('时间输入有误！，请重新输入')
            check_ticket()
    except:
        print('输入的站台有误，请重新输入！')
        check_ticket()

    url = 'https://kyfw.12306.cn/otn/leftTicket/queryZ?leftTicketDTO.train_date=' + date + '&leftTicketDTO.from_station=' + from_station_code + '&leftTicketDTO.to_station=' + to_station_code + '&purpose_codes=ADULT'
    response = SESSION.get(url)
    response.encoding = 'utf-8'
    try:
        station_dict = json.loads(response.text)
    except:
        print('ERROR，信息获取错误，重新连接！')
        check_ticket()
    result = station_dict['data']['result']
    res_map = station_dict['data']['map']

    for station in result:
        station = station.split('|')
        print('**********************************************************')
        # 显示列车详情
        from_station = res_map[station[6]]
        to_station = res_map[station[7]]
        for i in range(len(station)):
            if station[i] == '':
                station[i] = '--'

        print('''时间:%s    车次:%s    出发站-到达站:%s-%s    出发时间-到达时间:%s-%s    历时:%s''' % (
            date, station[3], from_station, to_station, station[8], station[9], station[10]))
        print('''
        商务座、特等座:%s
        一等座:%s
        二等座:%s
            软卧:%s
            硬卧:%s
            硬座:%s
            无座:%s
        ''' % (station[32], station[31], station[30], station[23], station[28], station[29], station[26]))


def main():
    if os.path.isfile(FILENAME):
        pass
    else:
        station_name()
    check_ticket()


if __name__ == '__main__':
    main()