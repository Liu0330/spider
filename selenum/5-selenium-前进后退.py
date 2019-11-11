# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.keys import  Keys

url = 'http://www.baidu.com'

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(url)
    driver.find_element_by_id('kw').send_keys('小米9')
    driver.find_element_by_id('su').send_keys(Keys.ENTER)
    time.sleep(2)
    driver.back()
    time.sleep(2)
    driver.forward()
    driver.quit()
