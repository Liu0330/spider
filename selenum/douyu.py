from selenium import webdriver
import  time

url = 'https://www.douyu.com/directory/all'

# 动态html网页加载可能出现的问题：element is not attached to the page document
# 标签没有及时的加载显示出来，如果加载时间不够，可能报错
# try except

class Douyu(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def start(self):
        self.driver.get(url)
        time.sleep(2)
        self.driver.find_element_by_class_name('pop-zoom-close').click()
        fp = open('douyu.txt', 'w', encoding='utf-8')
        with open('douyu.html','w',encoding='utf-8') as file:
            file.write(self.driver.page_source)
        while False:
            titles = self.driver.find_elements_by_css_selector('h3.ellipsis')
            nums = self.driver.find_elements_by_xpath('//span[@class="dy-num fr"]')
            print(len(titles),len(nums))
            for title,num in zip(titles[10:],nums):
                print('标题是：%s，观战人数：%s'%(title.text.strip(),num.text.strip()))
                fp.write('标题是：%s，观战人数：%s'%(title.text.strip(),num.text.strip())+'\n')
            '''<a href="#" class="shark-pager-next shark-pager-disable shark-pager-disable-next">
            下一页</a>
            <a href="#" class="shark-pager-next">下一页</a>
            '''
            # 如果没有找到flag = -1
            # 找到了，返回索引值
            flag = self.driver.page_source.find('shark-pager-disable-next')
            if flag != -1:
                break

            # 选中的当前页码
            '''<a href="#" class="shark-pager-item current">1</a>'''

            current_page = self.driver.find_element_by_xpath('//a[@class="shark-pager-item current"]').text

            print('当前页码是：',current_page)
            try:
                self.driver.find_element_by_class_name('shark-pager-next').click()

                time.sleep(2)
            except:
                time.sleep(2)

        # 点击进入最后一页
        # xpath多重条件查询，直接后面添加[][]
        self.driver.find_element_by_xpath('//a[contains(@class,"shark-pager-item")][last()]').click()


        fp.close()
        time.sleep(10)
        self.driver.quit()



if '__main__' == __name__:
    douyu = Douyu()
    douyu.start()
