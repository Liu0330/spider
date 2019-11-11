# -*- coding: utf-8 -*-
# @Time    : 2019/05/07 14:25
# @Author  : Liu
# @File    : 04_yanzhengma.py


from PIL import Image
import pytesseract
image = Image.open('1.png')#输入自己想识别图片的路径
# 指定路径，路径为安装的OCR对应的目录
text = pytesseract.image_to_string(image,lang='chi_sim',)
print(text)