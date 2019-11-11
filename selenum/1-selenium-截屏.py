# -*- coding: utf-8 -*-
from time import time, sleep

from selenium  import webdriver


url = 'http://www.qq.com/'

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='D:\PYTHON3.6\chromedriver.exe')
    driver.get(url)
    sleep(1)
    driver.maximize_window()#窗口最大化
    driver.save_screenshot('./qq.png')
    driver.close()



