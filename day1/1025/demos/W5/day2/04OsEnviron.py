#! C:\Users\wangshuai\AppData\Local\Programs\Python\Python35\python.exe
# coding:utf-8
'''
about what
'''
import os

# 告诉浏览器，接下来要输出的是普通文本（而非HTML）
print("Content-type:text/plain")
print()#必须的空行

print("=====以下是服务器信息=====")
env = os.environ
for key in env.keys():
    print(key,env[key])