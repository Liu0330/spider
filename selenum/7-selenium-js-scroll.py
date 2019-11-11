from selenium import webdriver
from selenium.webdriver import ChromeOptions
url = 'https://pc.xuexi.cn/points/login.html'
import time

if __name__ == '__main__':
    options = ChromeOptions()
    # options
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.get(url)
    driver.set_window_size(500,500)
    time.sleep(3)
    # js = 'document.documentElement.scrollTop=10000'
    js = 'window.scrollTo(400,document.body.scrollHeight-750)'
    driver.execute_script(js)
    time.sleep(5)
    driver.quit()