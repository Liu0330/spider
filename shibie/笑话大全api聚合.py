# # -*- coding: utf-8 -*-
import json, urllib
from urllib import urlencode



def main():
    # 配置您申请的APPKey
    appkey = "*********************"

    # 1.按更新时间查询笑话
    request1(appkey, "GET")

    # 2.最新笑话
    request2(appkey, "GET")

    # 3.按更新时间查询趣图
    request3(appkey, "GET")

    # 4.最新趣图
    request4(appkey, "GET")


# 按更新时间查询笑话
def request1(appkey, m="GET"):
    url = "http://japi.juhe.cn/joke/content/list.from"
    params = {
        "sort": "",  # 类型，desc:指定时间之前发布的，asc:指定时间之后发布的
        "page": "",  # 当前页数,默认1
        "pagesize": "",  # 每次返回条数,默认1,最大20
        "time": "",  # 时间戳（10位），如：1418816972
        "key": appkey,  # 您申请的key

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])

        else:
            print("%s:%s" % (res["error_code"], res["reason"]))

    else:
        print("request api error")



# 最新笑话
def request2(appkey, m="GET"):
    url = "http://japi.juhe.cn/joke/content/text.from"
    params = {
        "page": "",  # 当前页数,默认1
        "pagesize": "",  # 每次返回条数,默认1,最大20
        "key": appkey,  # 您申请的key

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print( res["result"])

        else:
            print("%s:%s" % (res["error_code"], res["reason"])
)
    else:
        print("request api error")



# 按更新时间查询趣图
def request3(appkey, m="GET"):
    url = "http://japi.juhe.cn/joke/img/list.from"
    params = {
        "sort": "",  # 类型，desc:指定时间之前发布的，asc:指定时间之后发布的
        "page": "",  # 当前页数,默认1
        "pagesize": "",  # 每次返回条数,默认1,最大20
        "time": "",  # 时间戳（10位），如：1418816972
        "key": appkey,  # 您申请的key

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(res["result"])

        else:
            print("%s:%s" % (res["error_code"], res["reason"]))

    else:
        print("request api error")



# 最新趣图
def request4(appkey, m="GET"):
    url = "http://japi.juhe.cn/joke/img/text.from"
    params = {
        "page": "",  # 当前页数,默认1
        "pagesize": "",  # 每次返回条数,默认1,最大20
        "key": appkey,  # 您申请的key

    }
    params = urlencode(params)
    if m == "GET":
        f = urllib.urlopen("%s?%s" % (url, params))
    else:
        f = urllib.urlopen(url, params)

    content = f.read()
    res = json.loads(content)
    if res:
        error_code = res["error_code"]
        if error_code == 0:
            # 成功请求
            print(   res["result"])

        else:
            print("%s:%s" % (res["error_code"], res["reason"]))

    else:
        print("request api error")



if __name__ == '__main__':
    main()