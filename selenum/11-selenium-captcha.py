# -*- coding: utf-8 -*-
from selenium import webdriver
from  PIL import Image
url = 'http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx/'

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    driver.maximize_window()

    img = driver.find_element_by_id('imgCode')
    loc = img.location
    size = img.size



