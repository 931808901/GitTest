#! C:\Python36\python.exe
# coding:utf-8
'''
创建进程
'''
import multiprocessing
import os
import threading

import time


def countNumbers(num):
    # 打印子进程id、名称、父进程ID
    pid = multiprocessing.current_process().pid
    pname = multiprocessing.current_process().name
    ppid = os.getppid()
    print("进程ID%d,进程名称%s，他的父进程ID是%d" % (pid, pname, ppid))

    for i in range(1, num + 1):
        print(pname + ":", i)
        time.sleep(1)


def helloMultiPorcess():
    # 打印CPU核数
    print("劳资的CPU是%d核的" % (multiprocessing.cpu_count()))
    # 打印主进程信息
    mainProcess = multiprocessing.current_process()
    print("主进程的ID是%d，名称是%s" % (mainProcess.pid, mainProcess.name))
    # 创建子进程（设置为守护进程）并运行
    # def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):
    p = multiprocessing.Process(target=countNumbers, args=(10,))
    p.daemon = True  # 设置子进程为守护进程
    p.start()
    time.sleep(3)
    print("main over")


def activeChildren():
    p = multiprocessing.Process(target=countNumbers, args=(10,))
    p.start()
    multiprocessing.Process(target=countNumbers, args=(10,)).start()
    # 在主进程中判断子进程是否存活
    time.sleep(3)
    print("子进程活着吗？", p.is_alive())
    # 获取当前活动子进程列表
    print("当前活动进程列表：", multiprocessing.active_children())

class CountProcess(multiprocessing.Process):
    def __init__(self,num):
        super(CountProcess, self).__init__()
        self.num = num

    def run(self):
        countNumbers(self.num)

if __name__ == "__main__":
    helloMultiPorcess()
    # activeChildren()

    # 使用继承法实现数数进程
    # CountProcess(5).start()

    print("main over")
