import requests
import json
from bs4 import BeautifulSoup
import time


class hotComments:
    def __init__(self):
        self.headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
        }

    # offset页数,limit一页显示最多的评论数
    def get_hotComments(self, music_id):
        self.url = "http://music.163.com/api/v1/resource/comments/R_SO_4_{}?offset=0&limit=50".format(music_id)
        try:
            self.text = json.loads(requests.get(self.url, headers=self.headers).text)
            datas = self.text['hotComments']
        except:
            print("没有找到该歌曲的热评")
            return
        print("\n\n\n" + "网易云热评:   " + "--------" * 20 + "\n\n\n")
        for content in datas:
            print(content['content'])
        print("\n\n\n" + "---分--界--线----" * 20)

    def get_music_id(self, urls=None):
        try:
            html = requests.get(urls, headers=self.headers).text
        except:
            print("请输入正确的网址!!!")
            return
        text = BeautifulSoup(html, 'lxml')
        ids = text.select('.f-hide li a')
        # print(text)
        for id in ids:
            music_id = id.get('href').split('=')[1]
            self.get_hotComments(music_id)
            time.sleep(1)


if __name__ == '__main__':
    music = hotComments()
    while True:
        print("""
        网易云获取热评：
            1. 通过歌曲的ｉｄ
            2. 通过歌单的连接
            0. 退出
        """)
        number = 0
        try:
            number = int(input("请输入：　"))
        except:
            input("请输入数字")
        if number == 2:
            song_url = input("请输入歌单的网址: ")
            song_url = song_url.replace('/#', '')
            # print(song_url)
            music.get_music_id(urls=song_url)
        elif number == 1:
            id = input("请输入歌曲的id: ")
            music.get_hotComments(id)
        elif number == 0:
            exit()
        else:
            print("没有该选项")