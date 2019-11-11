# -*- coding:utf-8 -*-
import requests

# 发送请求
# response = requests.get("https://jingyan.baidu.com/event/img/jdqsspzj252.jpg")
# # 保存
# with open("a.jpg", "wb") as f:
#     f.write(response.content)
# 获取网页数据的方法
# response.content.decode() : bytes
# response.content.decode("gbk")
# response.text :str text是属性不是方法

response = requests.get("https://m.weibo.cn/api/container/getIndex?type=uid&value=3267187212&containerid=1076033267187212&since_id=4360257751302636")
# response1= response.content.decode()
# print(response1)
with open("weibo1.txt", "w", encoding="utf-8") as r:
    r.write(response.content.decode())
    print("ok")

f2 = open("weibo1.txt", 'rb').read() #二进制方式打开
f2.decode().encode().decode("gbk")
print(f2)