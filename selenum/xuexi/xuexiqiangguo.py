import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common import exceptions
from selenium.webdriver.chrome.options import Options
from threading import Thread
import requests
import json
import os
import re

def user():
    # name = input("请输入用户名: ")
    name = '18513106743'
    return name

def login():
    print(datetime.now(), "程序开启")
    driver.get("https://pc.xuexi.cn/points/login.html")
    driver.execute_script('window.scrollTo(document.body.scrollWidth/2 - 200 , document.body.scrollHeight-800)')
    print(datetime.now(), "此刻请扫描二维码...")
    WebDriverWait(driver, 270).until(EC.title_is(u"我的学习"))
    driver.get("https://pc.xuexi.cn/points/my-points.html")
    cookies = driver.get_cookies()
    readnum, videonum, readtime, videotime = readpoint(driver)
    learn_main(cookies, readnum, videonum, readtime, videotime)

def readpoint(driver):
    WebDriverWait(driver, 30).until(lambda driver: driver.find_element_by_class_name("my-points-card-text"))
    points = driver.find_elements_by_class_name("my-points-card-text")
    readnum = int(points[1].text.split("/")[1][:-1]) - int(points[1].text.split("/")[0][:-1])
    videonum = int(points[2].text.split("/")[1][:-1]) - int(points[2].text.split("/")[0][:-1])
    readtime = (int(points[3].text.split("/")[1][:-1]) - int(points[3].text.split("/")[0][:-1])) * 4
    videotime = (int(points[4].text.split("/")[1][:-1]) - int(points[4].text.split("/")[0][:-1])) * 5
    print("阅读文章得分{}，需要再学习{}篇文章".format(points[1].text, readnum))
    print("观看视频得分{}，需要再学习{}个视频".format(points[2].text, videonum))
    print("文章学习时长得分{}，需要再学习{}分钟文章".format(points[3].text, readtime))
    print("视频学习市场得分{}，需要再学习{}分钟视频".format(points[4].text, videotime))
    return readnum, videonum, readtime, videotime

def get_list():
    if os.path.exists("./user/{}/log.txt".format(user_name)):
        print("历史学习记录读取成功")
        print("后台学习即将开始...")
    else:
        with open("./user/{}/log.txt".format(user_name), "w", encoding="utf8")as fp:
            fp.write("0")
        get_list()
    with open("./user/{}/log.txt".format(user_name), "r", encoding="utf8") as fp:
        log = int(fp.read())
    article = requests.get(
        "https://www.xuexi.cn/c06bf4acc7eef6ef0a560328938b5771/data9a3668c13f6e303932b5e0e100fc248b.js").content.decode(
        "utf8")
    video = requests.get(
        "https://www.xuexi.cn/4426aa87b0b64ac671c96379a3a8bd26/datadb086044562a57b441c24f2af1c8e101.js").content.decode(
        "utf8")
    return log, article, video

def learn_article(cookies, readnum, readtime, log, article):
    driver.quit()
    options = Options()
    options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    options.add_argument('--mute-audio')  # 关闭声音
    options.add_argument('--window-size=400,500')
    options.add_argument('--headless')
    driver_article = webdriver.Chrome(chrome_options=options)  # 实例化chrome

    driver_article.get("https://pc.xuexi.cn/points/my-study.html")  # 读取上下文
    driver_article.delete_all_cookies()  # 删除未登陆cookie
    for cookie in cookies:  # 添加cookies
        driver_article.add_cookie({k: cookie[k] for k in {'name', 'value', 'domain', 'path'}})

    links = []
    pattern = r"list\"\:(.+),\"count\"\:"
    list = re.search(pattern, article)
    for i in range(log, log + readnum):
        links.append(eval(list.group(1))[i]["static_page_url"])
    for i in range(readnum):
        driver_article.get(links[i])
        for j in range(4 * 60):
            driver_article.execute_script(
                'window.scrollTo(0, document.body.scrollHeight/240*{})'.format(j))
            print("\r正在多线程学习中，文章剩余{}秒".format(readtime - j), end="")
            time.sleep(1)
        driver_article.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        readtime -= 4 * 60
    driver_article.get(eval(list.group(1))[0]["static_page_url"])
    for i in range(readtime):
        time.sleep(1)
        print("\r正在多线程学习中，文章剩余{}秒".format(readtime - i), end="")
        driver_article.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    print("文章学习完成")
    return driver_article

def learn_video(cookies, videonum, videotime, log, video):
    options = Options()
    # C:\Program Files (x86)\Google\Chrome\Application
    options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    options.add_argument('--mute-audio')  # 关闭声音
    options.add_argument('--window-size=400,500')
    options.add_argument('--headless')
    driver_video = webdriver.Chrome(chrome_options=options)  # 实例化chrome
    driver_video.get("https://pc.xuexi.cn/points/my-study.html")  # 读取上下文
    driver_video.delete_all_cookies()  # 删除未登陆cookie
    for cookie in cookies:  # 添加cookies
        driver_video.add_cookie({k: cookie[k] for k in {'name', 'value', 'domain', 'path'}})
    pattern = r'https://www.xuexi.cn/[^,"]*html'
    link = re.findall(pattern, video, re.I)
    link.reverse()
    print("=" * 30)
    links = []
    for i in range(log, log + videonum):
        links.append(link[i])
    for i in range(videonum):
        driver_video.get(links[i])
        for j in range(5 * 60):
            driver_video.execute_script(
                'window.scrollTo(0, document.body.scrollHeight/240*{})'.format(j))
            print("\r正在多线程学习中，视频剩余{}秒".format(videotime - j), end="")
            time.sleep(1)
        driver_video.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        videotime -= 5 * 60
    driver_video.get(link[log])
    for i in range(videotime):
        time.sleep(1)
        print("\r正在多线程学习中，视频剩余{}秒".format(videotime - i), end="")
        driver_video.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    print("视频学习完成")
    driver_video.quit()

def learn_main(cookies, readnum, videonum, readtime, videotime):
    log, article, video = get_list()
    logwrite = log + 6
    with open("./user/{}/log.txt".format(user_name), "w", encoding="utf8")as fp:
        json.dump(logwrite, fp)
    hour_now = datetime.now().hour
    print(datetime.now())
    t2 = Thread(target=learn_video, args=(cookies, videonum, videotime * 60, log, video))
    t2.start()
    driver_article = learn_article(cookies, readnum, readtime * 60, log, article)
    t2.join()
    print("学习完毕")

    driver_article.get("https://pc.xuexi.cn/points/my-points.html")
    print("学习完毕，学习情况如下，30分钟后程序自动关闭")
    readpoint(driver_article)
    driver_article.quit()
    time.sleep(60 * 5)

if __name__ == '__main__':
    user_name = user()
    options = Options()
    options.binary_location = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe"
    options.add_argument('blink-settings=imagesEnabled=false')  # 不加载图片, 提升速度
    options.add_argument('--mute-audio')  # 关闭声音
    options.add_argument('--window-size=400,500')
    options.add_argument('--window-position=800,0')
    driver = webdriver.Chrome(chrome_options=options)  # 实例化chrome
    login()
