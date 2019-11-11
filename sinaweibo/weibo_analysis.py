import csv
import pandas as pd
import jieba.analyse


def get_ciyun(city):    #进行分词
    tags=jieba.analyse.extract_tags(str(city),topK=100,withWeight=True)
    for item in tags:
        print(item[0]+'\t'+str(int(item[1]*1000)))


need_citys = ['北京', '上海', '湖南', '四川', '广东']
beijing = []
shanghai = []
hunan = []
sichuan = []
gd = []
pd.set_option('expand_frame_repr', True)    #可换行显示
pd.set_option('display.max_rows', None)    #显示所有行
pd.set_option('display.max_columns', None)    #显示所有列
df = pd.read_csv('C:\\Users\LiuWang\Desktop\【信息学院】学生工作信息统计表(1).xlsx')    #读取文件内容并转化为dataframes对象

contents = df['first_news']    #取微博内容
city = df['city']    #取城市
for i in range(len(city)):
    if need_citys[0] in city[i]:    #判断并存入
        beijing.append(contents[i])
    elif need_citys[1] in city[i]:
        shanghai.append(contents[i])
    elif need_citys[2] in city[i]:
        hunan.append(contents[i])
    elif need_citys[3] in city[i]:
        sichuan.append(contents[i])
    elif need_citys[4] in city[i]:
        gd.append(contents[i])
    else:
        pass

#输出
get_ciyun(beijing)
print('-'*20)
get_ciyun(shanghai)
print('-'*20)
get_ciyun(hunan)
print('-'*20)
get_ciyun(sichuan)
print('-'*20)
get_ciyun(gd)