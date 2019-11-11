# -*- coding: utf-8 -*-
# @Time    : 2019/09/06 16:01
# @Author  : Liu
# @File    : 12输出文件目录.py
import os
filePath = r'H:\GPpython'
for i,j,k in os.walk(filePath):
    print(i,j,k)