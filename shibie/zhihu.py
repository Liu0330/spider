# -*- coding: utf-8 -*-
# @Time    : 2019/07/15 20:18
# @Author  : Liu
# @File    : zhihu.py
import requests
import os
import time
from threading import Thread
import threadpool
import traceback
import tkinter
from tkinter import *
import threading
from tkinter import messagebox
import win32clipboard as wc
from tkinter import filedialog


def async(f):
    def wrapper(*args, **kwargs):
        thr = Thread(target=f, args=args, kwargs=kwargs)
        thr.start()

    return wrapper


class zhihu(object):
    def __init__(self):
        self.id = None
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'
        }
        self.zh_id = 1
        self.zx_id = 1
        self.nm_id = 1
        self.cz_id = 1
        self.stop_num = 0

        # 创建主窗口,用于容纳其它组件
        self.root = tkinter.Tk()

        # 给主窗口设置标题内容
        self.root.title("知乎问题图片/视频下载器")
        width = 440
        height = 500

        # 获取屏幕尺寸以计算布局参数，使窗口居屏幕中央
        screenwidth = self.root.winfo_screenwidth()
        screenheight = self.root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        self.root.geometry(alignstr)
        self.root.resizable(width=False, height=False)

        self.var = StringVar()
        self.label_tips = tkinter.Label(self.root, textvariable=self.var, justify=CENTER, font=("微软雅黑", 12, "bold"),
                                        fg='red')
        # self.var.set('正在下载，请稍等... (共433个回答)')

        self.ok_var = StringVar()
        self.label_ok = tkinter.Label(self.root, textvariable=self.ok_var, justify=CENTER, font=("微软雅黑", 10, "bold"),
                                      fg='Firebrick')
        # self.ok_var.set('已完成 13%')

        self.input_var = StringVar()
        self.label_wtid = tkinter.Label(self.root, text='请输入问题ID或问题链接：')
        self.input_wtid = tkinter.Entry(self.root, textvariable=self.input_var, width=37)
        self.button_wtzt = tkinter.Button(self.root, text="粘贴", width=6, command=self.getCopyTxet)

        self.wt_file_var = StringVar()
        self.wt_file_var.set('D:/ZhiHu')
        self.label_wt_file = tkinter.Label(self.root, text='请选择保存目录：')
        self.input_wt_file = tkinter.Entry(self.root, textvariable=self.wt_file_var, state=DISABLED, width=37)
        self.button_wt_file = tkinter.Button(self.root, text="更改", width=6, command=self.thread_browse_folder)

        self.button_wtjc = tkinter.Button(self.root, text="检测", width=8, command=self.thread_wenti_jc,
                                          font=("微软雅黑", 12, "bold"))
        self.Monitor_button = tkinter.Button(self.root, text="下载", width=8, command=self.thread_get_offset,
                                             font=("微软雅黑", 12, "bold"))
        self.label_tips1 = tkinter.Label(self.root, text='使用说明：')
        self.label_tips2 = tkinter.Label(self.root, text='1.下载前请先检测问题，以免下错资源')
        self.label_tips3 = tkinter.Label(self.root, text='2.问题资源为实时下载，你可随时在下载文件夹查看')
        # self.label_tips4 = tkinter.Label(self.root, text='3.更多好玩软件、资源欢迎')

    def gui_arrang(self):

        self.label_tips.place(x=52, y=28)

        self.label_wtid.place(x=55, y=82)
        self.input_wtid.place(x=55, y=114)
        self.button_wtzt.place(x=329, y=110)

        self.label_wt_file.place(x=55, y=146)
        self.input_wt_file.place(x=55, y=178)
        self.button_wt_file.place(x=329, y=174)

        self.button_wtjc.place(x=60, y=220)
        self.Monitor_button.place(x=164, y=220)
        self.label_ok.place(x=300, y=233)

        self.label_tips1.place(x=55, y=334)
        self.label_tips2.place(x=55, y=360)
        self.label_tips3.place(x=55, y=386)
        # self.label_tips4.place(x=55, y=412)

    # 获取粘贴板里的内容
    def getCopyTxet(self):
        try:
            wc.OpenClipboard()
            copytxet = wc.GetClipboardData()
            wc.CloseClipboard()
            self.input_var.set(str(copytxet))
        except:
            pass

    def thread_wenti_jc(self):
        t = threading.Thread(target=self.wenti_jc)
        t.setDaemon(True)
        t.start()

    def thread_get_offset(self):
        t = threading.Thread(target=self.get_offset)
        t.setDaemon(True)
        t.start()

    def thread_browse_folder(self):
        t = threading.Thread(target=self.browse_folder)
        t.setDaemon(True)
        t.start()

    # 浏览本地文件夹，选择保存位置
    def browse_folder(self):
        # 浏览选择本地文件夹
        save_address = filedialog.askdirectory()
        if len(save_address) != 0:
            self.wt_file_var.set(save_address)
        # 把获得路径，插入保存地址输入框（即插入input_save_address输入框）
        # input_save_address.insert(0, save_address)

    def wenti_jc(self):
        wt_data = self.input_wtid.get()
        if len(wt_data) == 0:
            tkinter.messagebox.showerror('错误提示', '请先输入问题ID或链接')
        else:
            try:
                if wt_data.isdigit():
                    url = 'https://www.zhihu.com/api/v4/questions/{}/answers'.format(wt_data)
                    r = requests.get(url, headers=self.headers)
                    if r.status_code == 200:
                        self.totals = int(r.json()['paging']['totals'])
                        self.title = r.json()['data'][0]['question']['title']
                        self.id = int(wt_data)
                        tkinter.messagebox.showinfo('问题ID正确', '你本次要下载的问题为“%s”' % self.title)
                    else:
                        tkinter.messagebox.showerror('问题ID输入错误', '请检查你的问题ID并重新输入')
                else:
                    wtids = re.findall('question/(.*?)/answer', wt_data)
                    if wtids and len(wtids[0]) != 0:
                        url = 'https://www.zhihu.com/api/v4/questions/{}/answers'.format(wtids[0])
                        r = requests.get(url, headers=self.headers)
                        if r.status_code == 200:
                            self.totals = int(r.json()['paging']['totals'])
                            self.title = r.json()['data'][0]['question']['title']
                            self.id = int(wtids[0])
                            tkinter.messagebox.showinfo('问题链接正确', '你本次要下载的问题为“%s”' % self.title)
                        else:
                            tkinter.messagebox.showerror('问题链接输入错误', '请检查你的问题链接并重新输入')
                    else:
                        if '/question/' in wt_data:
                            wtids = wt_data.split('/question/')
                            for wtid in wtids:
                                if wtid.isdigit():
                                    url = 'https://www.zhihu.com/api/v4/questions/{}/answers'.format(wtid)
                                    r = requests.get(url, headers=self.headers)
                                    if r.status_code == 200:
                                        self.totals = int(r.json()['paging']['totals'])
                                        self.title = r.json()['data'][0]['question']['title']
                                        self.id = int(wtid)
                                        tkinter.messagebox.showinfo('问题链接正确', '你本次要下载的问题为“%s”' % self.title)
                                    else:
                                        tkinter.messagebox.showerror('问题链接输入错误', '请检查你的问题链接并重新输入')
                        else:
                            tkinter.messagebox.showerror('问题链接输入错误', '请检查你的问题链接并重新输入')
            except:
                tkinter.messagebox.showerror('错误提示', '抱歉，出现未知错误，请稍后再试')

    def get_offset(self):
        if self.id == None:
            tkinter.messagebox.showerror('错误提示', '请先检测问题ID或链接是否正确')
        else:
            self.var.set('正在下载，请稍等... (共{}个回答)'.format(self.totals))
            self.Monitor_button.config(state=DISABLED)
            path = self.input_wt_file.get()
            self.file_path = '{}/{}'.format(path, self.title)
            folder = os.path.exists(self.file_path)
            if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
                os.makedirs(self.file_path)  # makedirs 创建文件时如果路径不存在会创建这个路径
            # else:
            #     print('该问题内容已经有啦~')
            #     sys.exit()
            if self.totals % 20 == 0:
                self.max = int(self.totals / 20)
            else:
                self.max = int(self.totals / 20) + 1
            for m in range(self.max):
                offset = m * 20
                self.get_urls(offset)
                time.sleep(3)

    # [url = home.php?mod = space & uid = 512266]
    #
    # @Async
    #
    # [ / url]  # 开启异步线程执行 调用一次开启一个线程
    def get_urls(self, offset):
        try:
            url = 'https://www.zhihu.com/api/v4/questions/{}/answers?include=data%5B*%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_labeled%3Bdata%5B*%5D.mark_infos%5B*%5D.url%3Bdata%5B*%5D.author.follower_count%2Cbadge%5B*%5D.topics&offset={}&limit=20&sort_by=updated'.format(
                self.id, offset)
            dict = {
                'include': 'data[*].is_normal,admin_closed_comment,reward_info,is_collapsed,annotation_action,annotation_detail,collapse_reason,is_sticky,collapsed_by,suggest_edit,comment_count,can_comment,content,editable_content,voteup_count,reshipment_settings,comment_permission,created_time,updated_time,review_info,relevant_info,question,excerpt,relationship.is_authorized,is_author,voting,is_thanked,is_nothelp,is_labeled;data[*].mark_infos[*].url;data[*].author.follower_count,badge[*].topics',
                'limit': 20,
                'offset': offset,
                'sort_by': 'updated'
            }
            r = requests.get(url, headers=self.headers, params=dict).json()
            if self.stop_num == 0:
                self.ok_var.set('已完成 1%')
            datas = r['data']
            for data in datas:
                content = data['content']
                name = data['author']['name']
                # 防止同天有多个匿名用户/已注销用户作答时文件名相同而覆盖操作
                if '知乎用户' == name:
                    name = '{}{}'.format(name, self.zh_id)
                    self.zh_id += 1
                if '「已注销」' == name:
                    name = '{}{}'.format(name, self.zx_id)
                    self.zx_id += 1
                if '匿名用户' == name:
                    name = '{}{}'.format(name, self.nm_id)
                    self.nm_id += 1
                if '[已重置]' == name:
                    name = '{}{}'.format(name, self.cz_id)
                    self.cz_id += 1
                timeStamp = int(data['updated_time'])
                timeArray = time.localtime(timeStamp)
                otherStyleTime = time.strftime("%Y-%m-%d", timeArray)
                img_names = []
                video_names = []
                img_urls = re.findall('<noscript><img src="(.*?)"', content, re.S)
                video_urls = re.findall('"z-ico-video"></span>(.*?)</span>', content, re.S)
                if img_urls:
                    for i in range(len(img_urls)):
                        file_name = '{}({})_{}'.format(name, otherStyleTime, i + 1)
                        img_names.append(file_name)
                    if len(img_urls) == len(img_names):
                        data = [((img_url, img_name), None) for (img_url, img_name) in
                                zip(img_urls, img_names)]  # (index,i)也可以写成[index,i]
                        pool = threadpool.ThreadPool(20)
                        results = threadpool.makeRequests(self.save_img, data)
                        [pool.putRequest(req) for req in results]
                        pool.wait()
                if video_urls:
                    for i in range(len(video_urls)):
                        file_name = '{}({})_video_{}'.format(name, otherStyleTime, i + 1)
                        video_names.append(file_name)
                    str_video_urls = str(video_urls)
                    video_ids = re.findall(".*?/video/(.*?)'", str_video_urls, re.S)
                    if len(video_ids) == len(video_names):
                        data = [((video_id, video_name), None) for (video_id, video_name) in
                                zip(video_ids, video_names)]  # (index,i)也可以写成[index,i]
                        pool = threadpool.ThreadPool(20)
                        results = threadpool.makeRequests(self.save_video, data)
                        [pool.putRequest(req) for req in results]
                        pool.wait()
            self.stop_num += 1
            ok_num = round(self.stop_num / self.max, 2)
            self.ok_var.set('已完成 {}%'.format(int(ok_num * 100)))
            if self.max == self.stop_num:
                tkinter.messagebox.showinfo('下载完成', '你的问题资源已全部下载完毕')
                self.var.set('')
                self.Monitor_button.config(state=NORMAL)
                self.ok_var.set('')
                self.zh_id = 1
                self.zx_id = 1
                self.nm_id = 1
                self.cz_id = 1
                self.stop_num = 0
        except:
            pass

    def save_img(self, img_url, img_name):
        suffix = None
        if '.jpg' in img_url:
            suffix = '.jpg'
        elif '.gif' in img_url:
            suffix = '.gif'
        try:
            img = requests.get(img_url, headers=self.headers)
            if img.status_code == 200:
                with open(self.file_path + '/' + img_name + suffix, "wb") as f:
                    f.write(img.content)
                # time.sleep(0.5)
            else:
                pass
        except:
            pass

    def save_video(self, video_id, video_name):
        try:
            url = 'https://lens.zhihu.com/api/v4/videos/{}'.format(video_id)
            video_url = requests.get(url, headers=self.headers).json()['playlist']['LD']['play_url']
            video = requests.get(video_url, headers=self.headers)
            if video.status_code == 200:
                with open(self.file_path + '/' + video_name + '.mp4', "wb") as f:
                    f.write(video.content)
                # time.sleep(0.5)
            else:
                pass
        except:
            print(traceback.format_exc())


def main():
    # 初始化对象
    L = zhihu()
    # 进行布局
    L.gui_arrang()
    # 主程序执行
    tkinter.mainloop()


if __name__ == '__main__':
    main()