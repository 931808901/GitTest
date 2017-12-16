#! C:\Python36\python.exe
# coding:utf-8
'''
·创建三条异步进程，并为其命名
·创建三条同步进程，并为其命名
·使用进程锁实现进程的同步
'''
import multiprocessing
import os

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


def processAsync():
    # 创建三条异步进程，令其数数，并为其命名
    pa = multiprocessing.Process(target=countNumbers, args=(10,), name="龙生号")
    pb = multiprocessing.Process(target=countNumbers, args=(10,), name="西门号")
    pc = multiprocessing.Process(target=countNumbers, args=(10,), name="采花号")
    pa.start()
    pb.start()
    pc.start()


def processSync():
    for i in range(3):
        p = multiprocessing.Process(target=countNumbers, args=(5,), name="小格-%d" % (i + 1))
        p.start()
        p.join()  # 阻塞主进程，直到p执行结束
        # 结束阻塞，继续运行


if __name__ == "__main__":
    # def __init__(self, group=None, target=None, name=None, args=(), kwargs={}):

    # processAsync()
    # processSync()

    print("main over")
