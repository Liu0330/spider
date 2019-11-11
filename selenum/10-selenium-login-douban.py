# -*- coding: utf-8 -*-
import time

from  selenium import webdriver
url ='http://douban.com'

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.get(url)
    iframe = driver.find_element_by_xpath('//div[@class="login"]/iframe')
    driver._switch_to.frame(iframe)

    account = driver.find_element_by_class_name('account-tab-account')
    account.click()
    driver.find_element_by_id('username').send_keys(username)
    driver.find_element_by_id('password').send_keys(pwd)
    driver.find_element_by_class_name('')
    # print(account)
    driver.quit()
