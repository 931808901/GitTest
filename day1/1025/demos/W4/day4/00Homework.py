#! C:\Python36\python.exe
# coding:utf-8
'''
从1加到一亿，使用单线程、10并发进程、10并发线程分别求其结果，统计并比较执行时间
@结论：
·效率对比：多进程 > 多线程 ≈ 单线程
·为什么多进程最快？
    多进程可以充分使用CPU【多核的并发计算能力】
·为什么多线程和点线程差不多？
    多线程是伪并发
·既然多线程在效率上与单线程相差无几，多线程存在的意义是什么？
    1、确实有多任务同时进行的需要
    2、平摊每条线程阻塞、抛异常的风险（试想主线程被阻塞时，逻辑全线瘫痪）
@ 多线程 VS 多进程
·进程的资源开销远远大于线程，能多线程解决的就不用多进程
·计算密集型用多进程，IO密集型（读写文件、数据库、访问网络等）用多线程
'''
import multiprocessing
import time

import threadpool


def getTotal(begin, stop, dataList=None):
    result = 0
    for num in range(begin, stop + 1):
        result += num

    # if dataList!=None:
    if dataList:
        dataList.append(result)

    return result


def singThread():
    start = time.time()
    result = getTotal(1, 10 ** 8)
    end = time.time()
    print(result, "耗时%.2f" % (end - start))


def multiProcessWay():
    start = time.time()
    with multiprocessing.Manager() as pm:
        dataList = pm.list()
        plist = []
        for i in range(10):
            p = multiprocessing.Process(target=getTotal, args=(i * 10 ** 7 + 1, (i + 1) * 10 ** 7, dataList))
            p.start()
            plist.append(p)

        for p in plist:
            p.join()

        result = 0
        for num in dataList:
            result += num
        end = time.time()
        print(result, "耗时%.2f" % (end - start))


totalResult = 0


def onResult(result):
    global totalResult
    totalResult += result


def onTpoolResult(req, result):
    global totalResult
    totalResult += result


def processPoolWay():
    start = time.time()
    myPool = multiprocessing.Pool(10)
    # def apply_async(self, func, args=(), kwds={}, callback=None,error_callback=None):
    for i in range(10):
        myPool.apply_async(getTotal, args=(i * 10 ** 7 + 1, (i + 1) * 10 ** 7), callback=onResult)
    myPool.close()
    myPool.join()
    end = time.time()
    print(totalResult, "耗时%.2f" % (end - start))


def threadPoolWay():
    start = time.time()
    arglist = []
    for i in range(10):
        arglist.append(([i * 10 ** 7 + 1, (i + 1) * 10 ** 7], None))
    reqThreads = threadpool.makeRequests(getTotal, arglist, callback=onTpoolResult)
    myPool = threadpool.ThreadPool(10)
    for rt in reqThreads:
        myPool.putRequest(rt)
    myPool.wait()
    end = time.time()
    print(totalResult, "耗时%.2f" % (end - start))


if __name__ == "__main__":

    # singThread()
    # multiProcessWay()
    # processPoolWay()
    # threadPoolWay()

    print("main over")
