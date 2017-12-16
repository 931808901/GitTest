#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import os
from cgi import FieldStorage

fs = FieldStorage()
user = fs.getvalue("user")
pwd = fs.getvalue("pwd")

print("Content-type:text/plain")
print()

print("宇宙非正常人类俱乐部欢迎您！%s阁下"%user)
print("请牢记您的密码：%s"%(pwd))