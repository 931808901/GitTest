#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import re

import pymysql
import requests


# 新闻url列表
urls = [
    "http://news.163.com/17/1029/11/D1TNDDET00018AOQ.html",
    "http://news.163.com/17/1029/21/D1UQ4AJQ0001899N.html",
    "http://news.163.com/17/1030/00/D1V2GUOL0001875P.html",
    "http://news.163.com/17/1029/23/D1V1QU730001875N.html",
    "http://news.163.com/17/1030/04/D1VHUD2T0001875P.html",
]

# 媒体正则
# 来源: <a ...>看看新闻Knews</a>
reMedia = "来源:\s*<a.+>(\w+)</a>"
reMedia = re.compile(reMedia)

# 标题正则
# <h1>美18岁少女抽大麻被捕 两名警察在警车内将其强奸</h1>
reTitle = "<h1.*>(.*)</h1>"
reTitle = re.compile(reTitle)

# 作者正则
# <span...>责任编辑：王征_B7526</span>
reAuthor = "<span.*>责任编辑：\s*(\w+)</span>"
reAuthor = re.compile(reAuthor)

# 发布时间正则
# 2017-10-29 21:39:38　来源:
reDate = "(\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2})\s+来源:"
reDate = re.compile(reDate)

# 邮箱正则
# sdfghj@sdzfg.aerty.agshdj
reEmail = "\w+@\w+\.\w+\.?\w*"
reEmail = re.compile(reEmail)

# 将新闻对象存入数据库
def saveNewsToDB(news):
    try:

        # 连接数据库并拿到查询游标
        conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="mynews",charset="utf8")
        cursor = conn.cursor()

        # 插入媒体信息
        try:
            rows = cursor.execute("insert into t_media(name) values('%s');"%(news.media))
            conn.commit()
            print("媒体插入成功")
        except Exception as e:
            print(e)

        # 插入作者信息
        try:
            # 先查询【新华网】的媒体ID
            rows = cursor.execute("select id from t_media where name='%s'"%(news.media))
            mediaId = cursor.fetchone()[0]

            # 插入作者信息，其中media_id媒体的外键
            rows = cursor.execute("insert into t_author(name,email,media_id) values('%s','%s',%d);"%(news.author,news.email,mediaId))
            conn.commit()
            print("作者插入成功")
        except Exception as e:
            print(e)

        # 插入文章信息
        try:
            # 先查询作者表，根据作者的名字得到其id，稍后这个id会作为文章表中作者的外键
            rows = cursor.execute("select id from t_author where name='%s'"%(news.author))
            authorId = cursor.fetchone()[0]

            # 插入文章信息，其中author_id是作者的外键，指向作者表中对应作者的id
            rows = cursor.execute("insert into t_article(url,title,publish_time,author_id) values('%s','%s','%s',%d);"%(news.url,news.title,news.publishTime,authorId))
            conn.commit()
            print("新闻插入成功")
        except Exception as e:
            print(e)


    except Exception as error:
        print(error)

    # 无论结果如何，最终关闭所有IO流
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()

# 新闻类
class News:

    # 由构造方法传递媒体、标题、作者、发布时间、邮箱
    def __init__(self,url,media,title,author,date,email):
        self.url = url
        self.media = media
        self.title = title
        self.author = author
        self.publishTime = date
        self.email = email

if __name__ == "__main__":

    # 遍历所有新闻
    for i in range(len(urls)):
        url = urls[i]

        # 拿到页面html代码
        html = requests.get(url).text
        # print(html)

        # 使用正则找出媒体、标题、作者、发布时间、邮箱
        mediaList = reMedia.findall(html)
        titleList = reTitle.findall(html)
        authorList = reAuthor.findall(html)
        dateList = reDate.findall(html)
        emailList = reEmail.findall(html)

        # 打印调试信息
        print(url)
        print(mediaList)
        print(titleList)
        print(authorList)
        print(dateList)
        print(emailList)

        # 直接传具体参数（最LOW的方式）
        # saveDataToDB(url,mediaList[0],titleList[0],authorList[0],dateList[0],emailList[0])

        # 封装信息为字典并传参（普通方式）
        # dataDict = {
        #     "url":url,
        #     "media":mediaList[0],
        #     "title":titleList[0],
        #     "author":authorList[0],
        #     "email":emailList[0],
        #     "date":dateList[0]
        # }
        # saveDataToDB(dataDict)

        # 封装为新闻对象并传参（最有逼格的方式）
        saveNewsToDB(News(url, mediaList[0], titleList[0], authorList[0], dateList[0], emailList[0] if len(emailList)>0 else None))

    print("main over")