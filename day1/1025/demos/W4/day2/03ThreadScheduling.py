#! C:\Python36\python.exe
# coding:utf-8
'''
线程调度:
·使用Semaphore控制最大并发数
·使用Barrier使线程分组执行（足三而行）
·延时执行线程
'''
import threading

import time


def sayHello():
    # 线程在执行时，必须先拿到Semaphore，从而保证线程的最大并发数控制在Semaphore规定的范围以内
    with sem:
        print(threading.current_thread().name + ":hello")
        time.sleep(1)


# 创建最大并发为3的Semaphore对象
sem = threading.Semaphore(3)


# 使用Semaphore控制最大并发数
def semaphoreDemo():
    for i in range(100):
        threading.Thread(target=sayHello).start()


# 创建一个足5而行的Barrier对象（攒够5条线程一起执行）
bar = threading.Barrier(5)


def passJingyanggang():
    try:
        # 阻塞到攒够5条线程才能过景阳冈
        # 如果等待超时，抛出BrokenBarrierError
        bar.wait(timeout=3)
    except threading.BrokenBarrierError:
        print(threading.current_thread().name + ":" + "休得阻拦爷爷！")

    # 攒够了Barrier对象所规定的线程数，线程得到执行
    print(threading.current_thread().name + "过了景阳冈")
    time.sleep(1)
    pass


# 使用Barrier使线程分组执行（足三而行）
def barrierDemo():
    for i in range(11):
        threading.Thread(target=passJingyanggang).start()


# 延执行线程
def timerDemo():
    # def __init__(self, interval, function, args=None, kwargs=None):
    threading.Timer(5, sayHello).start()


if __name__ == "__main__":
    semaphoreDemo()
    barrierDemo()
    timerDemo()

    print("main over")
