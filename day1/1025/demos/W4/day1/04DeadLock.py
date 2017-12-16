#! C:\Python36\python.exe
# coding:utf-8
'''
死锁
'''
import threading

import time

money = threading.Lock()
def func1():
    tname = threading.current_thread().getName()
    if money.acquire():
        print(tname,"独占了资本...")
        time.sleep(1)
        if tech.acquire():
            print(tname,"获得了技术")
            print(tname,"创业成功！")
            tech.release()
        money.release()

tech = threading.Lock()
def func2():
    tname = threading.current_thread().getName()
    if tech.acquire():
        print(tname, "独占了技术...")
        time.sleep(1)
        if money.acquire():
            print(tname, "获得了资本")
            print(tname, "创业成功！")
            money.release()
        tech.release()


def deadLock():
    threading.Thread(target=func1).start()
    threading.Thread(target=func2).start()

# RLock()所返回的是【可以在一条线程内反复加锁的锁】
mylock = threading.RLock()
def myfuck():
    with mylock:
        print("第一步已实现")
        with mylock:
            print("第二步已实现")
        print("大功告成！")

if __name__ == "__main__":
    # deadLock()
    # threading.Thread(target=myfuck).start()
    print("main over")