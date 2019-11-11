# coding=utf-8
from selenium import webdriver
import time
driver = webdriver.Chrome()
# driver.maximize_window()
driver.get("https://weibo.com/Liuwang1996/profile?is_all=1&stat_date=201904")
print(driver.page_source)
title_all =driver.find_elements_by_xpath("//div[@class='WB_text W_f14']")
for i in title_all:
    print(i.text)
#翻页
# driver.find_element_by_xpath("//button[@class='nav-btn iconfont icon-arrowdown3']").click()
time.sleep(3)

# print(driver.find_element_by_xpath("//ul[@class='vd-list mod-2']/li//a[@class='title']").text)

driver.quit()