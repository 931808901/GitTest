#! C:\Users\wangshuai\AppData\Local\Programs\Python\Python35\python.exe
# coding:utf-8
'''
处理页面发送过来的注册请求，并以HTML的形式输出结果
'''
import os
from cgi import FieldStorage

fs = FieldStorage()
user = fs.getvalue("user")
pwd = fs.getvalue("pwd")

# 声明以HTML格式输出
print("Content-type:text/html")
print()

# 输出头部信息
print('''
<head>
    <meta charset="gbk">
    <title>Title</title>
</head>
<body>
''')

print("宇宙非正常人类俱乐部欢迎您！<h3 style='color:red'>%s</h3>阁下"%user)
print("请牢记您的密码：<h3 style='color:#0000ff'>%s</h3>"%(pwd))

print("</body>")