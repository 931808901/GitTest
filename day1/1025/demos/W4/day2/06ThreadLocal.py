#! C:\Python36\python.exe
# coding:utf-8
'''
线程数据保险柜：threading.local()
允许不同线程存储名称相同的全局变量
'''
import threading

# 线程数据保险柜
import time

myLocal = threading.local()
def threadSaveData():
    # 在local保险柜的【自己的线程格子】里存放两个数据
    myLocal.name = "李四"
    myLocal.age = 30
    showData()

# 哪个线程来调用老夫
# 老夫就给它展示哪个线程格子里的数据
def showData():
    tname = threading.current_thread().name
    # 打开自己的线程格子，取出数据
    name = myLocal.name
    age = myLocal.age
    print("%s数据为：name=%s,age=%d"%(tname,name,age))

if __name__ == "__main__":

    threading.Thread(target=threadSaveData).start()

    # 在local保险柜的【自己的线程格子】里存放两个数据
    myLocal.name = "张三"
    myLocal.age = 20
    showData()

    print("main over")