# -*- coding: utf-8 -*-
# @Time    : 2019/05/05 11:46
# @Author  : Liu
# @File    : DOUBAN.py
import re
from  parse_url import parse_url

url = "http://36kr.com/"
html_str = parse_url(url)
print(html_str)
# print(type(html_str))


ret = re.findall("<script>var props=(.?)</script>",html_str)
print(ret)