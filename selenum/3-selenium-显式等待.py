# -*- coding: utf-8 -*-
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import  WebDriverWait

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.get('http://www.baidu.com/')
    try:
        kw = WebDriverWait(driver,10,0.5,
                      ).until(EC.presence_of_element_located((By.ID,'kw')))
        kw.send_keys("mac")
        # button =WebDriverWait(driver,10,0.5,
        #              ).until( EC.presence_of_element_located((By.CSS_SELECTOR, 'span[id=""]')))
        # button =WebDriverWait(driver,10,0.5,
        #              ).until( EC.presence_of_element_located((By.CSS_SELECTOR, '#su')))
        #xpath还没弄明白！！
        button =WebDriverWait(driver,10,0.5,
                     ).until( EC.presence_of_element_located((By.XPATH, '//span[@id="s_btn_wr]/input"]')))
        button.click()
    except:
        print("等待十秒无加载结果")
    finally:
        time.sleep(5)
        driver.quit()
