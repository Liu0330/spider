# -*- coding: utf-8 -*-
import time

from selenium import webdriver
url = 'https://www.douban.com/'

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    driver.get(url)
    movie_link = driver.find_element_by_link_text('豆瓣电影')
    movie_link.click()
    time.sleep(5)
    windows =driver.window_handles
    # driver.switch_to_window(windows[1]) 更新
    driver._switch_to.window(windows[1])
    book_element = driver.find_element_by_xpath('//div[@class="global-nav-item/ul"]')
    book_element.click()
