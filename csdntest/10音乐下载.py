#!/usr/bin/env python
# -*- coding: utf-8 -*-
# [url=home.php?mod=space&uid=238618]@Time[/url]    : 2018/7/20 14:37
# [url=home.php?mod=space&uid=686208]@AuThor[/url]  : Bnightning
# [url=home.php?mod=space&uid=406162]@site[/url]    : https://www.bnightning.cn
# [url=home.php?mod=space&uid=267492]@file[/url]    : douqq.py
# @Software: PyCharm
import requests
import json

headers = {
    'Host': 'c.y.qq.com',
    'Referer': 'http://c.y.qq.com/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 '
                  'Safari/537.36 '
}


def douqq_post(mid):
    """
    返回歌曲下载url
    :param mid:歌曲mid
    :return: 字典
    """
    post_url = 'http://www.douqq.com/qqmusic/qqapi.php'
    data = {'mid': mid}
    res = requests.post(post_url, data=data)
    get_json = json.loads(res.text)
    return eval(get_json)


def download_file(src, file_path):
    """
    歌曲下载
    :param src: 下载链接
    :param file_path: 存储路径
    :return: 文件路径
    """
    r = requests.get(src, stream=True)
    f = open(file_path, "wb")
    for chunk in r.iter_content(chunk_size=512):
        if chunk:
            f.write(chunk)
    return file_path


def choice_download(dic):
    print('1. m4a视频')
    print('2. mp3普通品质')
    print('3. mp3高品质')
    print('4. ape高品无损')
    print('5. flac无损音频')
    select = int(input("Please input your choice:"))
    src = ''
    postfix = ''
    if select == 1:
        src = dic['m4a']
        postfix = '.m4a'
    if select == 2:
        src = dic['mp3_l']
        postfix = '.mp3'
    if select == 3:
        src = dic['mp3_h']
        postfix = '.mp3'
    if select == 4:
        src = dic['ape']
        postfix = '.ape'
    if select == 5:
        src = dic['flac']
        postfix = '.flac'
    return postfix, src.replace('\/\/', '//').replace('\/', '/')


def find_song(word):
    """
    查找歌曲
    :param word: 歌曲名
    :return: 返回歌曲mid
    """
    get_url = 'https://c.y.qq.com/soso/fcgi-bin/client_search_cp?&t=0&aggr=1&cr=1&catZhida=1&lossless=0&flag_qc=0&p=1&n' \
              '=20&w=' + word
    res1 = requests.get(get_url, headers=headers)
    get_json = json.loads(res1.text.strip('callback()[]'))
    jsons = get_json['data']['song']['list']
    songmid = []
    media_mid = []
    song_singer = []
    i = 1
    for song in jsons:
        # print(i, ':' + song['songname'], '---', song['singer'][0]['name'], song['songmid'], song['media_mid'])
        print(i, ':' + song['songname'], '---', song['singer'][0]['name'])
        songmid.append(song['songmid'])
        media_mid.append(song['media_mid'])
        song_singer.append(song['singer'][0]['name'])
        i = i + 1
    select = int(input("Please input your choice:")) - 1
    return songmid[select], song_singer[select]


if __name__ == '__main__':
    # songname = '叹云兮'
    songname = input("Please input the music name:")
    song_mid, singer = find_song(songname)
    dic = douqq_post(song_mid)
    # {
    # "mid":"004FjJo32TISsY",
    # "m4a":"http:\/\/dl.stream.qqmusic.qq.com\/C400004FjJo32TISsY.m4a?guid=2095717240&vkey=0B599CA74745F8A27A33A1FED2C7F6925FFFE8ED040569FB3540EB011FE9C5A3D7F36EAE4BDBD450F25076A23EBAF95A5ECB54B22C5E8F10&uin=0&fromtag=38",
    # "mp3_l":"http:\/\/dl.stream.qqmusic.qq.com\/M500004FjJo32TISsY.mp3?guid=2095717240&vkey=0B599CA74745F8A27A33A1FED2C7F6925FFFE8ED040569FB3540EB011FE9C5A3D7F36EAE4BDBD450F25076A23EBAF95A5ECB54B22C5E8F10&uin=0&fromtag=53",
    # "mp3_h":"http:\/\/dl.stream.qqmusic.qq.com\/M800004FjJo32TISsY.mp3?guid=2095717240&vkey=0B599CA74745F8A27A33A1FED2C7F6925FFFE8ED040569FB3540EB011FE9C5A3D7F36EAE4BDBD450F25076A23EBAF95A5ECB54B22C5E8F10&uin=0&fromtag=53",
    # "ape":"http:\/\/dl.stream.qqmusic.qq.com\/A000004FjJo32TISsY.ape?guid=2095717240&vkey=0B599CA74745F8A27A33A1FED2C7F6925FFFE8ED040569FB3540EB011FE9C5A3D7F36EAE4BDBD450F25076A23EBAF95A5ECB54B22C5E8F10&uin=0&fromtag=53",
    # "flac":"http:\/\/dl.stream.qqmusic.qq.com\/F000004FjJo32TISsY.flac?guid=2095717240&vkey=0B599CA74745F8A27A33A1FED2C7F6925FFFE8ED040569FB3540EB011FE9C5A3D7F36EAE4BDBD450F25076A23EBAF95A5ECB54B22C5E8F10&uin=0&fromtag=53",
    # "pic":"https:\/\/y.gtimg.cn\/music\/photo_new\/T002R300x300M000003NZyTh4eMMsp.jpg?max_age=2592000"
    # }
    # print('mid:'+dic['mid'])
    postfix, url = choice_download(dic)
    save_path = "H:\\Music\\"
    download_file(url, save_path + songname + ' - ' + singer + postfix)
    print('Download Successful')