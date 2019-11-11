from selenium import webdriver
import pytesseract
from PIL import Image
import time

url = 'https://so.gushiwen.org/user/login.aspx?from=http://so.gushiwen.org/user/collect.aspx'

def get_captcha():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    driver.get(url)
    # 元素
    img = driver.find_element_by_id('imgCode')
    driver.save_screenshot('./poem.png')
    image = Image.open('./poem.png')

    # 左上角坐标
    loc = img.location
    print(loc)
    # 图片宽度高度
    size = img.size
    print(size)
    # 矩形区域
    # 160,260
    # 234,291
    rec = (loc['x']+100 , loc['y']+51, 554, 290)
    captcha = image.crop(rec)
    # 保存到文件中
    captcha.save('./captcha.png')
    return driver


def recognize_captcha():
    captcha = Image.open('./captcha.png')
    gray = captcha.convert('L')
    data = gray.load()
    w,h = captcha.size
    for x in range(w):
        for y in range(h):
            # 0 ~ 255 0纯黑，255纯白
            if data[x,y] < 140:
                data[x,y] = 0
            else:
                data[x,y] = 255
    code = pytesseract.image_to_string(gray)
    return code


def login(drive,code):
    drive.find_element_by_id('email').send_keys('455098435@qq.com')
    drive.find_element_by_id('pwd').send_keys('31415926abc')
    drive.find_element_by_id('code').send_keys(code)
    time.sleep(3)
    drive.find_element_by_id('denglu').click()

if __name__ == '__main__':
    drive = get_captcha()
    # code验证码，有可能出错
    code = recognize_captcha()
    # print('----------------',code)
    login(drive,code)
    drive.quit()