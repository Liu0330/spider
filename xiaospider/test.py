import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://www.w3school.com.cn/')
# print(driver.page_source)
print('=================================')

for i in driver.find_elements_by_css_selector('h2'):
    print(i.text)

driver.quit()