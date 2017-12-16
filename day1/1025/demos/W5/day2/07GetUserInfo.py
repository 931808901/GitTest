#! C:\Users\wangshuai\AppData\Local\Programs\Python\Python35\python.exe
# coding:utf-8
'''
给客户端输出JSON信息
'''
import json
from cgi import FieldStorage

if __name__ == "__main__":

    # 获取请求参数
    fs = FieldStorage()
    id = fs.getvalue("id")

    # 模拟查询到用户数据
    data = {"id":id,"name":"暗黑破坏神","password":"123456"}
    dataJson = json.dumps(data)
    # print(type(dataJson))

    # 向客户端输出数据
    print("Content-type:text/plain")
    print()

    print(dataJson)