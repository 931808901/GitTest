#! C:\Python36\python.exe
# coding:utf-8
'''
·创建一个3并发的进程池
·丢入5条任务各异的异步进程，
·关闭进程池并令主进程等待子进程执行完毕
·以回调函数处理结果和异常
·池中全部进程结束后，打印执行结果
apply(...),apply_async(...)，close()，join()
----------
·如法炮制执行5条同步进程
·池中全部进程结束后，打印执行结果
'''
import multiprocessing
import os

import time


def kill(whom, price, why="凡人皆有一死"):
    pname = multiprocessing.current_process().name
    print("%s正在杀死【%s】,价格是%.2f,原因是【%s】" % (pname, whom, price, why))
    time.sleep(3)
    print("well done！%s" % (pname))

    if whom.isdigit():
        raise RuntimeError("名字不合法")

    if len(whom) < 5:
        return "已成功杀死%s" % (whom)
    else:
        return "失败，%s名字太长记不住" % (whom)

def countNumbers(num):
    # 打印子进程id、名称、父进程ID
    pid = multiprocessing.current_process().pid
    pname = multiprocessing.current_process().name
    ppid = os.getppid()
    print("进程ID%d,进程名称%s，他的父进程ID是%d" % (pid, pname, ppid))

    for i in range(1, num + 1):
        print(pname + ":", i)
        time.sleep(1)

    # raise RuntimeError("心情不好，抛个异常")
    return "countNumbers Over!"

def onResult(result):
    pname = multiprocessing.current_process().name
    print("onResult@%s"%(pname), result)

def onError(error):
    pname = multiprocessing.current_process().name
    print("onError@%s"%(pname),error)


def processPoolAsync():
    # 创建一个3并发的进程池
    myPool = multiprocessing.Pool(3)
    # 丢入5条"任务各异"的异步进程
    # 以回调函数处理结果和异常
    # def apply_async(self, func, args=(), kwds={}, callback=None,error_callback=None):
    # def kill(whom, price, why="凡人皆有一死")
    myPool.apply_async(countNumbers, args=(5,), callback=onResult, error_callback=onError)
    myPool.apply_async(kill, args=("阿雄", 10000.00), kwds={"why": "长得太帅"}, callback=onResult, error_callback=onError)
    myPool.apply_async(countNumbers, args=(10,), callback=onResult, error_callback=onError)
    myPool.apply_async(kill, args=("123456", 30000.00), kwds={"why": "代码太牛逼"}, callback=onResult,error_callback=onError)
    myPool.apply_async(kill, args=("阿杰", 30000.00), kwds={"why": "代码太牛逼"}, callback=onResult, error_callback=onError)
    # 关闭进程池并令主进程等待子进程执行完毕
    myPool.close()
    myPool.join()


def processPoolSync():
    # 开辟3并发的进程池
    myPool = multiprocessing.Pool(3)
    # 丢入4条同步进程
    ret1 = myPool.apply(countNumbers, args=(5,))  # 阻塞的等待结果
    print(ret1)
    ret2 = myPool.apply(kill, args=("阿雄", 10000.00), kwds={"why": "长得太帅"})  # 阻塞的等待结果
    print(ret2)
    ret3 = myPool.apply(countNumbers, args=(10,))  # 阻塞的等待结果
    print(ret3)
    ret4 = myPool.apply(kill, args=("阿杰", 30000.00), kwds={"why": "代码太牛逼"})  # 阻塞的等待结果
    print(ret4)
    # 关池行刑
    myPool.close()
    myPool.join()


if __name__ == "__main__":
    processPoolAsync()
    # processPoolSync()

    print("main over")