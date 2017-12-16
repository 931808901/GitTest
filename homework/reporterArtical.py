#! C:\Users\wangshuai\AppData\Local\Programs\Python\Python35\python.exe
# coding:utf-8

import json
from cgi import FieldStorage

import pymysql


def searchArtical(id):
    conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='world',
                           charset='utf8')
    cur = conn.cursor()
    sql='select * from articles a,reporter r where a.reporterid=r.reporterid and r.name like "%'+id+'%"'
    cur.execute(sql)
    # cur.execute('select * from articles a,reporter r where a.reporterid=r.reporterid and r.name like "%%s%"' % (id))
    info = cur.fetchall()
    cur.close()
    conn.close()
    return info


if __name__ == "__main__":

    # 获取请求参数
    fs = FieldStorage()
    id = fs.getvalue("id")
    # id='王敌'
    # 查询记者文章
    info=searchArtical(id)

    print("Content-type:text/plain")
    print()

    print(info)
