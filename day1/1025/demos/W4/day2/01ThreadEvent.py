#! C:\Python36\python.exe
# coding:utf-8
'''
线程通信之Event
模拟鼠标点击
'''
import threading
from threading import Thread

import time

class MouseClick:
    def __init__(self,order,user):
        self.order = order
        self.user = user


class User(Thread):
    def __init__(self,event,mcList):
        super().__init__()
        self.event = event
        self.name = "User"
        self.mcList = mcList

    def  run(self):
        time.sleep(3)

        for i in range(5):
            # 发布事件
            mc = MouseClick(i,self.name)
            self.mcList.append(mc)

            self.event.set()
            print("User:我第%d次点鼠标"%(i))
            time.sleep(1)

class Os(Thread):
    def __init__(self,event,mcList):
        super().__init__()
        self.event = event
        self.mcList = mcList

    def run(self):
        # 循环监听用户事件
        while True:
            # 阻塞，监听事件
            event.wait()
            # 收到事件
            mc = self.mcList.pop(0)

            # 处理事件
            print("Os:响应%s第%d次点击"%(mc.user,mc.order))
            event.clear()




if __name__ == "__main__":
    event = threading.Event()
    mcList = []
    User(event,mcList).start()
    Os(event,mcList).start()

    print("main over")