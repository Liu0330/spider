# -*- coding: utf-8 -*-
# import time
#
# from selenium  import webdriver
# from selenium.webdriver.common.by import By
#
# url = 'http://www.taobao.com/'
#
# if __name__ == '__main__':
#     driver = webdriver.Chrome(executable_path='D:\PYTHON3.6\chromedriver.exe')
#     driver.get(url)
#     driver.implicitly_wait(5)#弹性等待
#     driver.find_element_by_xpath('//input[@id="q"]').send_keys('macbook pro')
#     driver.find_element_by_css_selector('div[class="search-button"] > button').click()
#     time.sleep(2)
#
#     driver.quit()

# -*- coding: utf-8 -*-
import time

from selenium  import webdriver
from selenium.webdriver.common.by import By

url = 'http://www.baidu.com/'

if __name__ == '__main__':
    driver = webdriver.Chrome(executable_path='D:\PYTHON3.6\chromedriver.exe')
    driver.implicitly_wait(5)#弹性等待
    driver.get(url)

    driver.find_element_by_xpath('//input[@class="s_ipt"]').send_keys('macbook pro')
    driver.find_element_by_css_selector('span[class="bg s_btn_wr"] > input').click()
    time.sleep(5)

    driver.quit()


