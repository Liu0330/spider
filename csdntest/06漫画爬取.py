import requests
import time
import json
import re
import os
import img2pdf
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from fake_useragent import UserAgent
from urllib.parse import urlencode, urljoin, unquote
from lxml import etree
from threading import Thread

base_url = 'https://www.manhuatai.com/'
headers = {
    'referer': 'https://www.manhuatai.com/',
    'user-agent': UserAgent(verify_ssl=False).random,

}


# 搜索接口，返回搜索列表
def get_search_items(keyword):
    """
    :param keyword:
    :return:
    """
    headers.update({
        'x-requested-with': 'XMLHttpRequest'
    })
    params = {
        'd': int(time.time()),
        'q': keyword,
    }
    params = urlencode(params)
    res = requests.get('https://www.manhuatai.com/getjson.shtml?', headers=headers, params=params).content.decode(
        'utf-8')
    results = json.loads(res)
    print('-' * 20, '搜索结果:', '-' * 20, '\n')
    for index, item in enumerate(results):
        print('编号：{}'.format(index))
        print('名字：{}'.format(item['cartoon_name']))
        print('id：{}'.format(item['cartoon_id']))
        print('状态：{}'.format(item['cartoon_status_id']))
        print('最新章节：{}'.format(item['latest_cartoon_topic_name']))
        print('=' * 50)
    return results


# 获取所搜索的漫画章节列表
def get_comic_list(cartoon_name, remove_fw=False):
    url = urljoin(base_url, cartoon_name)
    res = requests.get(url, headers=headers).content.decode('utf-8')
    # print(res)
    doc = etree.HTML(res)
    c_img = doc.xpath('//*[@id="offlinebtn-container"]/img/@data-url')[0]
    c_name = doc.xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/ul/li[1]/text()')[0]
    c_status = doc.xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/ul/li[2]/text()')[0]
    c_author = doc.xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/ul/li[3]/text()')[0]
    c_type = doc.xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/ul/li[4]/text()')[0]
    c_update = doc.xpath('/html/body/div[1]/div[3]/div/div[1]/div/div[2]/div[2]/ul/li[5]/text()')[0]
    print(c_img, '\n', c_name, '\n', c_status, '\n', c_author, '\n', c_type, '\n', c_update)

    # 获取所有下载链接
    chapter_list = doc.xpath('//*[@id="topic1"]/li/a/@href')[::-1]
    # print(chapter_list, chapter_list[::-1])
    # if remove_fw:
    #     chapter_list = list(filter(lambda x: isinstance(int, x.split('/')[-1].split('.')[0]), chapter_list))
    # chapter_list_ = list()
    if remove_fw:
        for index, item in enumerate(chapter_list):
            if item.split('/')[-1].split('.')[0][:2] == 'fw':
                # print(item)
                del chapter_list[index]

    # print(chapter_list)
    return chapter_list


# 分析解析规则并批量下载
def get_parse_format(r_url):
    url = urljoin(base_url, r_url)
    driver.get(url)
    source = driver.page_source
    # print(source)
    img_url = re.search('<img src="(.*?)"', source).group(1)
    total_page_num = re.search('<option value="1" selected="">第1/(\d+)页</option>', source).group(1)
    # 引  ||  第8话  ||  8话GQ
    re_text = re.search('(.*?)/comic/(.*?)%2F(.*?)%2F(.*?)%E8%AF%9D(.*?)%2F(\d+).jpg-', img_url)
    try:
        mh_domain = re_text.group(1)
        mh_tou = re_text.group(2)
        mh_name = re_text.group(3)
        mh_cp_num = unquote(re_text.group(4))
        mh_char = re_text.group(5)
        # mh_num = re_text.group(6)
        # print(total_page_num, mh_domain, mh_tou, mh_name, mh_cp_num, mh_char, mh_num)
        for i in range(1, int(total_page_num) + 1):
            t = Thread(target=download, args=(mh_domain, mh_tou, mh_name, mh_cp_num, mh_char, i,))
            t.start()
    except AttributeError:
        print('\n')
        print('非正文图片：{}'.format(url))


def download(mh_domain, mh_tou, mh_name, mh_cp_num, mh_char, i):
    url = '{}/comic/{}%2F{}%2F{}%E8%AF%9D{}%2F{}.jpg-mht.middle.jpg'.format(mh_domain, mh_tou, mh_name, mh_cp_num,
                                                                            mh_char, i)
    # [img]https://mhpic.manhualang.com/comic/D%2F%E6%96%97%E7%BD%97%E5%A4%A7%E9%99%86%E6%8B%86%E5%88%86%E7%89%88%2F%E7%95%AA%E5%A4%96%E7%AF%8722GQ%2F1.jpg[/img]-mht.middle.webp
    res = requests.get(url, headers=headers).content
    cp_num, sec_num = re.search('(\d+)', mh_cp_num).group(1), i
    if len(mh_cp_num) < 3:
        cp_num = '0' * (3 - len(cp_num)) + cp_num
    if i < 1000:
        sec_num = '0' * (3 - len(str(i))) + str(i)
    with open('./{}/第{}话-{}节.jpg'.format(dir_name, cp_num, sec_num), 'wb') as f:
        f.write(res)


# 打包成pdf
def pack_to_pdf(dir_name):
    a4inpt = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
    layout_fun = img2pdf.get_layout_fun(a4inpt)
    file_list = list()
    for root, dirs, files in os.walk(dir_name):
        for file in files:
            if file.endswith('.jpg'):
                pathname1 = os.path.join(root, file)
                file_list.append(pathname1)
    file_lis_list = list()
    while file_list:
        try:
            file_lis_list.append(file_list[:501])
            del file_list[:501]
        except IndexError:
            file_lis_list.append(file_list[:-1])
            del file_list[::]

    for index, item in enumerate(file_lis_list):
        try:
            with open('{}/{}.pdf'.format(dir_name, index + 1), 'wb') as f:
                f.write(img2pdf.convert(item, layout_fun=layout_fun))

        except Exception as e:
            print(e.args)
            print('第{}个打包失败~~┭┮﹏┭┮~~'.format(index + 1))
        else:
            print('第{}个打包成功<(*￣▽￣*)/！'.format(index + 1))


def process(index, length):
    current_num = int((index + 1) / length * 50)
    total_num = 50
    return '>' * current_num + '*' * (total_num - current_num)


def main():
    while True:
        search_words = input('请输入你要查找的内容：>>')
        search_results = get_search_items(search_words)
        if search_results:
            break
        else:
            print('没有查到你要找的漫画，请重新搜索')
    choice = input('请选择要下载第几个？（选择对应漫画的编号）')
    global dir_name, driver
    dir_name = search_results[int(choice)]['cartoon_name']
    if not os.path.exists(dir_name):
        os.mkdir(dir_name)
    mh_list = get_comic_list(search_results[int(choice)]['cartoon_id'], '(⊙o⊙)…' != '')
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    print('正在启动驱动程序...')

    driver = webdriver.Chrome(executable_path='chromedriver.exe', options=options)
    length = len(mh_list)
    for mh_i, mh in enumerate(mh_list, 1):
        # print('\r正在下载：{}第{}/{}话'.format(mh_i, length), end='')
        print('\r正在下载：[{}]第{}/{}话'.format(process(mh_i, length), mh_i, length), end='')
        get_parse_format(mh)
    print('\n下载完成，正在打包中...')
    pack_to_pdf(dir_name)


if __name__ == '__main__':
    main()