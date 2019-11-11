# coding:utf-8
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