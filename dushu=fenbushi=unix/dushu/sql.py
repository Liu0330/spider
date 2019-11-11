import pymysql

conn = pymysql.Connect(host = '10.0.102.120',port = 3306,
                user = 'root',password = 'liuwang',
                database = 'books_gp02',charset='utf8')

print(conn)

cursor = conn.cursor()

insert = 'insert into book(book_url,book_name,book_author,book_info) ' \
         'values("%s","%s","%s","%s")'%('https://img.dushu.com/2013/03/27/02471452731601.jpg_200.jpg',
                                        '闲愁万种',
                                        '胡兰成',
                                        '该书由朱天文亲自编定，收录旅居日本时的十一篇散文，五十三篇诗作，二十八则书句，或记事，或言情，或抒志，可视作自传《今生今世》的续篇补记。另收有两篇理论文章《民志篇》《劫毁篇》，论述中国历史上民间起兵的传统和机缘。最后的《日月并明》是胡兰成未完绝笔，其中探讨男女文明之起源和区别，为胡兰成晚年独特的文化见解。')

print(cursor.execute(insert))

conn.commit()#数据执行时，必须提交操作，起作用

cursor.close()
conn.close()
