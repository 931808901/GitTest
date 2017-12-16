#coding=utf-8
import threading

import time

data=0
money=threading.Lock()
tech=threading.Lock()
def fun1():
    tname=threading.current_thread().getName()
    if money.acquire():
        print('%s获得资本'%tname)
        time.sleep(1)
        if tech.acquire(timeout=3):
            print('fun1 sucess')
            tech.release()
        else:
            print('fun1 failed')
        money.release()
def fun2():
    tname=threading.current_thread().getName()
    if tech.acquire():
        time.sleep(1)
        print('%s 获得技术'%tname)
        if money.acquire():
            print('fun2 sucess')
            money.release()
        tech.release
threading.Thread(target=fun1).start()
threading.Thread(target=fun2).start()