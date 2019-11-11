from tkinter import *
from re import findall, sub
from tkinter.ttk import Combobox
from requests import get, post

headers = {
    'Cookie': 'Tip_of_the_day=2; encrypt_data=56f2bc9d081609eb8e605a176c9f144de8c9c6ac96288a2e51fce7143a94433d8c0c4fc70944b9163392d9ea977fc7343168112d1769b16d03bd4b9d7d56317224940c2824ccbeeccb73a633bdfeabdd7c124ff7f5064b6ef27b7959ebcb279cb52e5da22eff1a00fd6ee3efe7adc077a415e7bd0edfb126ed4487ef27904634; SL_GWPT_Show_Hide_tmp=1; SL_wptGlobTipTmp=1',
    'Host': 'moresound.tk',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}


def huoqu(urlid):
    url = 'http://moresound.tk/music/' + urlid
    res = get(url, headers=headers)
    ress = res.json()
    ff = ress[url]
    # print(ff)
    return ff


def Save(urlid):
    url = huoqu(urlid)
    res = get(url).content
    Save_wenjian = sub('[\\\\/:*?\"<>|]', '', str(Save_name))  # 正则去掉文件名不支持的字符
    with open('{}.{}'.format(Save_wenjian, dict_yinzhi[yinzhiyinqin]), 'wb')as f:
        f.write(res)

    confirmLabel.insert(END, '已保存至本程序运行的文件下！！!!', '\n\n请继续搜索下载')


def danqu_url(id):
    global Save_name
    url = 'http://moresound.tk/music/api.php?get_song={}'.format(sousuo_key)
    data = {'mid': id}
    res = post(url, data=data, headers=headers)
    ss = res.json()
    global yinzhi_key
    global dict_yinzhi
    global yinzhiyinqin
    yinzhiyinqin = xialalan01.get()  # 获取输入的音质

    dict_yinzhi = {'无损FLAC': 'flac', '无损压缩APE': 'ape', '128品质MP3': 'mp3', '128品质WMA': 'wma', '48品质AAC': 'aac'}

    yinzhi_key = dict_yinzhi[yinzhiyinqin]
    if yinzhi_key == "aac":
        try:
            yinzhi_key = ss['url']['48AAC']
        except:
            confirmLabel.insert(END, '没有48AAC音质的', '\n\n试试别的音质的')
    elif yinzhi_key == 'mp3':
        try:
            yinzhi_key = ss['url']['128MP3']
        except:
            confirmLabel.insert(END, '没有128MP3音质的', '\n\n试试别的音质的')

    elif yinzhi_key == 'flac':

        try:
            yinzhi_key = ss['url']['FLAC']
        except:
            confirmLabel.insert(END, '没有FLAC音质的', '\n\n试试别的音质的')
    elif yinzhi_key == 'ape':

        try:
            yinzhi_key = ss['url']['APE']
        except:
            confirmLabel.insert(END, '没有APE音质的', '\n\n试试别的音质的')
    elif yinzhi_key == 'wma':

        try:
            yinzhi_key = ss['url']['128WMA']
        except:
            confirmLabel.insert(END, '没有128WMA音质的', '\n\n试试别的音质的')
    else:
        return null
    Save_name = str(ss['song']) + '--' + str(ss['singer'])
    Save(yinzhi_key)


id_list = []  # 用于将sousuo()函数获取到的歌曲ID装起来


def sousuo():
    global sousuo_key
    sousuoyinqin = xialalan.get()  # 获取输入的搜索引擎

    dict_sousuo = {'QQ': 'qq', '酷我': 'kw', '酷狗': 'kg', '百度': 'bd', '网易': 'wy', '咪咕': 'mg'}

    sousuo_key = dict_sousuo[sousuoyinqin]  # 确认选择的搜索引擎
    del id_list[:]  # 清空列表，重置（使用多次以后列表装太多数据，不删除下次会出错）
    confirmLabel.delete(0, END)  # 清空文本框
    dd = namee_Entry.get()  # 获取输入的歌名
    url = 'http://moresound.tk/music/api.php?search={}'.format(sousuo_key)
    data = {
        'w': '{}'.format(dd),
        'p': '1',
        'n': '20',
    }
    res = post(url, data=data, headers=headers)
    ress = res.json()
    for i in range(20):
        name_geshou = ress['song_list'][i]['singer'][0]['name']
        name_geming = ress['song_list'][i]['songname']
        name_zhuanji = ress['song_list'][i]['albumname']
        name_id = ress['song_list'][i]['songmid']

        name_geming1 = sub('<sup.*|\n|\r|', '', str(name_geming)[:10])  # 去掉多余的信息
        isserts = name_geshou + '  ' + name_geming1 + '  专辑：  ' + name_zhuanji
        confirmLabel.insert(END, str(i) + ':' + isserts)  # 将获取到的详细信息打印到GUI
        id_list.append(name_id)  # 获取到的id添加到列表里面，供xuanze(event)函数使用。


def xuanze(event):
    ff = confirmLabel.get(confirmLabel.curselection())
    ff = findall('\d+', str(ff))
    # print(id_list[ii],ii)
    confirmLabel.delete(0, END)  # 清空文本框
    confirmLabel.insert(END, '准备下载：请稍后...')
    window.update()
    if ff != []:
        ii = int(ff[0])
        danqu_url(id_list[ii])


window = Tk()
weather = StringVar()
window.geometry('800x600+500+200')  # 窗口大小
window.title('歌曲下载===下载速度取决于您的网速')

taitouLabel = Label(window, text="请输入要下载的歌曲名或歌手名:  ", height=1, width=30, font=("Times", 20, "bold"), fg='red')
sousuoLabel = Label(window, text="选择音乐库:  ", height=1, width=10, font=("Times", 15, "bold"), fg='#00008b')
xialalan = Combobox(window, width=4, textvariable=weather, font=("黑体", 18, "bold"), state='editable')
xialalan['values'] = ('QQ', '酷我', '酷狗', '百度', '网易', '咪咕')
xialalan.current(2)

sousuoLabel01 = Label(window, text="选择音质:  ", height=1, width=10, font=("Times", 12, "bold"), fg='#00008b')
xialalan01 = Combobox(window, width=10, font=("黑体", 12, "bold"), state='editable')
xialalan01['values'] = ('无损FLAC', '无损压缩APE', '128品质MP3', '128品质WMA', '48品质AAC')
xialalan01.current(0)

namee_Entry = Entry(window, width=25, font=("Times", 20, "bold"))

button = Button(window, text="搜索", command=sousuo, )  # .grid_location(33,44)
GunDongTiao = Scrollbar(window)  # 设置滑动块组件
confirmLabel = Listbox(window, height=15, width=55, font=("Times", 15, "bold"), fg='red', bg='#EEE5DE',
                       yscrollcommand=GunDongTiao.set)  # Listbox组件添加Scrollbar组件的set()方法
confirmLabel.bind('<Double-Button-1>', xuanze)  # 双击选择文本框的内容
GunDongTiao.config(command=confirmLabel.yview)  # 设置Scrollbar组件的command选项为该组件的yview()方法
taitouLabel.grid(column=1)
sousuoLabel.grid(row=0, column=0)
xialalan.grid(row=1, column=0)
sousuoLabel01.grid(row=2, column=0)
xialalan01.grid(row=3, column=0)
namee_Entry.grid(row=1, column=1, sticky=N + S)
button.grid(row=1, column=1, sticky=E)

confirmLabel.grid(row=4, column=1, sticky=E)
GunDongTiao.grid(row=4, column=2, sticky=N + S + W)  # 设置垂直滚动条显示的位置
window.mainloop()