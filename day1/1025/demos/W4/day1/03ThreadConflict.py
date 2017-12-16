#! C:\Python36\python.exe
# coding:utf-8
'''
线程冲突
'''

import threading

import time

data = 0
def add():
    global data
    for i in range(1000000):
        data += 1
    print("data=",data)

dataLock = threading.Lock()
def addWithLock():
    tname = threading.current_thread().getName()
    print(tname, "正在执行addWithLock...")
    global data
    # 申请独占锁资源
    if dataLock.acquire():#本行是【阻塞】的
        # 拿到锁资源
        print(tname,"拿到锁资源")
        for i in range(1000000):
            data += 1
        time.sleep(1)

        # 访问结束，释放锁资源
        print(tname,"释放锁资源")
        dataLock.release()

    print("data=",data)

def addWithLockII():
    tname = threading.current_thread().getName()
    print(tname, "正在执行addWithLock...")
    global data

    # 申请并使用dataLock资源，用完自动释放
    with dataLock:
        print(tname,"拿到dataLock")
        for i in range(1000000):
            data += 1
        time.sleep(1)
        print("data=", data)

    print(tname,"释放了dataLock")

# 5条线程并发修改data，造成结果不正确
# 往往由于子线程没有完成阶段性成果就被夺走CPU执行权所致
def threadConflict():
    for i in range(5):
        threading.Thread(target=add).start()

# 通过线程同步的方式避免线程冲突
# 大家依次访问公共资源
def avoidConflictSync():
    for i in range(5):
        t = threading.Thread(target=add)
        t.start()
        t.join()

# 使用资源锁的方式避免线程冲突
def avoidConflictUsingLock():
    for i in range(5):
        # addWithLock方法中对资源的访问需要先拿到资源锁
        t = threading.Thread(target=addWithLock)
        t.start()


def avoidConflictUsingLockII():
    for i in range(5):
        t = threading.Thread(target=addWithLockII)
        t.start()


if __name__ == "__main__":
    threadConflict()
    avoidConflictSync()
    avoidConflictUsingLock()
    avoidConflictUsingLockII()
    print("main over")