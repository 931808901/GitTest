#! C:\Python36\python.exe
# coding:utf-8
'''
author=张三
·接收作者参数
·查询作者的全部文章
·输出在页面上
'''
from cgi import FieldStorage

import pymysql

'''
#查询某作者的全部文章
SELECT a.`title`
FROM t_article a JOIN t_author b ON a.`author_id`=b.id
WHERE b.name LIKE '李天奕%';
'''

# 根据作者名称查询作者的全部文章
def queryAuthorArticls(authorName):
    # 自动将作者名称模糊处理
    authorName = "%"+authorName+"%"

    # 连接数据库并获取查询游标
    conn = pymysql.connect(host='localhost',port=3306,user="root",password="123456",db='mynews',charset="utf8")
    cursor = conn.cursor()

    # 执行查询
    rows = cursor.execute("SELECT a.title FROM t_article a JOIN t_author b ON a.author_id=b.id WHERE b.name LIKE '%s';"%(authorName))
    retList = cursor.fetchall()

    # 关闭IO
    cursor.close()
    conn.close()

    # 返回结果
    return retList

if __name__ == "__main__":

    # 先从请求中获取author参数
    fs = FieldStorage()
    authorName = fs.getvalue("author")
    # print(authorName)

    # 调用方法查询该作者的全部文章
    retTuple = queryAuthorArticls("李天奕")

    # 声明输出类型为普通文本而非HTML
    print("Content-type:text/plain")
    print()

    # 格式化输出结果
    print("以下是%s的文章列表："%(authorName))
    for article in retTuple:
        print(article[0])

    print("main over")