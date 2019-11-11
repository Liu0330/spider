# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")

#切换到iframe
driver.switch_to_frame("login_frame")


driver.find_element_by_id("u").send_keys("12312312312")


time.sleep(3)
driver.quit()