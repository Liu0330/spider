# -*- coding: utf-8 -*-
import time

from selenium import webdriver

# url = 'http://account.chinaunix.net/login'
url = 'http://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx/'


if __name__ == '__main__':
    username = "455098435@qq.com"
    password = "31415926abc"
    driver = webdriver.Chrome()
    driver.get(url)
    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pwd').send_keys(password)
    code = input("请输入验证码")
    driver.find_element_by_id('code').send_keys(code)
    driver.find_element_by_id('denglu').click()
    time.sleep(10)
    driver.quit()



