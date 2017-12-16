#! C:\Python36\python.exe
# coding:utf-8
'''
·使用Semaphore控制进程并发数
·使用Barrier是进程分组执行
'''
import multiprocessing
import os

import time

# 创建信号量对象
# sem属于主进程
sem = multiprocessing.Semaphore(3)

def countNumbers(num,sem):
    # 同时只能有3条进程拿到sem对象
    with sem:
        # 打印子进程id、名称、父进程ID
        pid = multiprocessing.current_process().pid
        pname = multiprocessing.current_process().name
        ppid = os.getppid()
        print("进程ID%d,进程名称%s，他的父进程ID是%d" % (pid, pname, ppid))

        for i in range(1, num + 1):
            print(pname + ":", i)
            time.sleep(1)

if __name__ == "__main__":

    # 创建7条进程，各自数10个数
    for i in range(7):
        multiprocessing.Process(target=countNumbers,args=(10,sem)).start()

    print("main over")