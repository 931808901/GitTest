#! C:\Python36\python.exe
'''
about what
'''
import csv
import os
import random
import threading

import re
from urllib import request

import requests
import time

from matplotlib import pyplot
# @基础语法（5分）
# ·写一个函数，判断输入的参数是否是素数；（素数只能被自身和1整除）

def isPrimeNumber(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# @函数和参数（5分）
# ·写出下面程序的执行结果
#     # 函数定义
#     def sayHello(name, age=20, *args, **kwargs):
#         print(name, age, args, kwargs)
#     # 函数调用
#     sayHello("fuck", 30, 40, 50, sex="男", gay=True)
def aPrimeNumber():
    for i in range(100):
        if isPrimeNumber(i):
            print(i)

# @模块（5分）
# ·导入系统模块math，写出导入语句
# ·导入math模块下的pow方法，写出导入语句
# ·系统库文件夹tkinter下的__init__.py下有Canvas类，现准备创建其对象，写出导入语句
def aModule():
    import math
    from math import pow
    from tkinter import Canvas

# @容器（5分）
# ·简述列表、元组、字典的区别
def aContainer():
    # 列表：有序，下标访问，append函数添加元素
    # 元组：有序，下标访问，只读
    # 字典：无序，通过键访问值，可以通过遍历items()或keys()访问
    pass

# @面向对象（10分）
# ·写一个银行账户类Account，构造对象时需要传递账号number、密码password
# ·密码属性是属性是私有的
# ·密码设置方法是私有的
# ·修改密码需要先校验密码格式（必须为6位整数），而该方法的调用无需创建对象
# ·对外提供修改密码方法,需要传递的参数为旧密码、新密码、重复新密码，写出完整的密码设置逻辑
class Account:
    def __init__(self, number, password):
        self.number = number
        self.__password = password

    def __setPassword(self, password):
        self.__password = password

    def changePassword(self, old, new, newAgain):
        if Account.canBePassword(new) and newAgain == new and old == self.__password:
            self.__password = new
            print("密码已成功修改为%d" % (new))

    @staticmethod
    def canBePassword(password):
        if password > 100000 and password < 999999:
            return True
        else:
            return False


def aOOP():
    acc = Account(123456, 654321)
    # print(acc.__password)
    # acc.__setPassword(111111)
    acc.changePassword(654321, 666666, 666666)
    print(Account.canBePassword(123456))


class PwdException(RuntimeError):
    def __init__(self, pwd):
        super().__init__()
        self.pwd = pwd

    def __str__(self):
        return "非法密码%s，长度应为6-12位"%(self.pwd)

# @异常处理（10分）
# ·写一个用户注册方法，要求输入昵称和密码
# ·如果密码长度不为6-12之间，则抛出一个自定义异常，提示“密码长度应为6-12位字符”
# ·调用该方法，并处理异常
def register(name, passwd):
    if len(passwd) < 6 or len(passwd) > 12:
        raise PwdException(passwd)
    else:
        print("注册成功！")


number = 0

# @文件操作（10分）
# ·写一个函数，传入一个文件夹路径，实现递归遍历并统计该文件夹下的文件数量
def getFileNumbers(path):
    global number
    files = os.listdir(path)
    for f in files:
        if os.path.isfile(path + f):
            number += 1
        else:
            getFileNumbers(path + f + "/")
    return number


def aFile():
    # print(os.path.isfile("D:/PyDownload"))
    # print(os.path.isfile(r"D:/PyDownload/csv/600000_浦发银行.csv"))
    # print(os.listdir(r"D:/PyDownload/csv/"))
    # print(getFileNumbers(r"D:/PyDownload/csv/"))
    print(getFileNumbers(r"D:/PyDownload/"))


def aException():
    try:
        register("hello", "1234")
    except Exception as e:
        print(e)

def sumRange(start,end,reslist):
    result = 0
    for i in range(start,end+1):
        result += i
    reslist.append(result)


def aThread():
    tlist = []
    reslist = []
    for i in range(1, 11):
        t = threading.Thread(target=sumRange, args=((i - 1) * 10000000 + 1, i * 10000000, reslist))
        tlist.append(t)
        t.start()
    for t in tlist:
        t.join()
    result = 0
    for res in reslist:
        result += res
    print("总合为", result)


def aFunction():
    # fuck,30,(40,50),{"sex":"男","gay":True}
    pass


def aRE():
    reId = "\d{6}-((19)|(20))\d{2}-((0\d)|((10)|(11)|(12)))-((0\d)|([12]\d)|((30)|(31)))-\d{3}[\dX]"
    rePhone = "1[3578]\d{9}"
    reEmail = "[a-z0-9][a-z0-9_]*@[a-z0-9_]*\.[a-z0-9_]*"
    print(re.match(reId, "340123-1990-07-04-1234"))
    print(re.match(rePhone, "13912345678"))
    print(re.match(reEmail, "abc12345@qq.com"))


def downloadImg(url,dirPath,imgname):
    if not os.path.isdir(dirPath):
        os.makedirs(dirPath)
    request.urlretrieve(url, dirPath + imgname)
    print(imgname,"下载完成")


def aSpider():
    html = requests.get("http://www.163.com").text
    urls = re.findall("<img .*src=\"(https?://.*?)\".*/>", html)
    for url in urls:
        imgname = str(time.time()) + "." + str(random.randint(100, 999)) + ".jpg"
        threading.Thread(target=downloadImg, args=(url, "D:/PyDownload/img/", imgname)).start()


def aOffice():
    with open(r"D:\PyDownload\csv\600036_招商银行.csv", "r") as file:
        freader = csv.reader(file)
        for item in freader:
            print(item)


def aSql():
    sTable = "create table tstudent(id integer primary key auto_increment,name varchar(20),age integer,class integer,enroll date);"
    sInsert = "insert into tstudent(name,age,class,enroll) values('zs',20,1,20170731);"
    sDelete = "delete from tstudent where age<20 and name like '张%';"
    sUpdate = "update tstudent set enroll=20170731 where id>0;"
    sQuery = "select * from tstudent order by name desc;"
    sQuery = "select class,count(id) as total from tstudent group by class having total>40 order by total desc;"


def aDataAnalysis():
    names = [1, 2, 3, 4, 5, 6, 7]
    data = [10, 30, 10, 40, 50, 20, 10]
    pyplot.bar(names, data)
    pyplot.show()
    pyplot.pie(data)
    pyplot.show()


def aLinux():
    '''
    cd ~/桌面
    mkdir hello
    touch ./hello/welcome.pylooooooooooooooooo                                                    tttttttttt
    gedit ./hello/welcome.py
    python3 welcome.py
    '''


if __name__ == "__main__":
    aPrimeNumber()
    aFunction()
    aModule()
    aContainer()
    aOOP()
    aException()
    aFile()

    aThread()
    aRE()
    aSpider()
    aOffice()
    aSql()
    aDataAnalysis()
    aLinux()

    print("main over")
