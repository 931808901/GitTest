#! C:\Python36\python.exe
# coding:utf-8
'''
线程池案例
'''
import threading

import threadpool
import time


def kill(whom):
    tname = threading.current_thread().name
    print("%s正在杀死%s..." % (tname, whom))
    time.sleep(3)
    print("well done,%s" % (tname))
    pass


def killProfessionally(whom, price, why="凡人皆有一死"):
    tname = threading.current_thread().name
    print("%s正在杀死【%s】,价格是%.2f,原因是【%s】" % (tname, whom, price, why))
    time.sleep(3)
    print("well done！%s" % (tname))
    pass


# 使用线程池执行一组参数不同的简单请求
def simpleRequestInPool():
    # 创建3容量的线程池对象
    myPool = threadpool.ThreadPool(3)
    # def makeRequests(callable_, args_list, callback=None,exc_callback=_handle_thread_exception)
    requests = threadpool.makeRequests(kill, ["约汉", "接客", "史密斯", "如花", "秋香"])
    # 向线程池对象中仍线程请求
    for req in requests:
        myPool.putRequest(req)

    # 阻塞等待池中的线程请求执行完毕
    myPool.wait()


# 使用线程池执行一组参数不同的复杂请求
def complexRequestInPool():
    # 线程执行的函数参数复杂，所以参数列表中的item为【两元素元祖】
    # 第一个元素为位置参数列表
    # 第二个元素为关键字参数字典
    arglist = [
        (["john", 0.50], {"why": "天天约汉"}),
        (["jack", 200.00], {"why": "天天接客"}),
        (["smith", 60000.00], {"why": "天天使人迷失"}),
        (["张三", 100.00], None),
    ]
    # 创建若干线程请求
    requests = threadpool.makeRequests(killProfessionally, arglist)
    # 创建3并发的线程池，执行上述请求
    myPool = threadpool.ThreadPool(3)
    for req in requests:
        myPool.putRequest(req)

    # 阻塞等待池中所有线程执行完毕
    myPool.wait()


# 故意在该函数中抛出异常
def killWithException(whom):
    tname = threading.current_thread().name
    print("%s正在杀死%s..." % (tname, whom))
    time.sleep(3)
    # ret = 5/0
    print("well done!%s" % (tname))

    if len(whom) < 3:
        return "已成功杀死%s" % (whom)
    else:
        return "失败，%s名字太长记不住" % (whom)


def handleKillException(req, exceptionInfo):
    print("handleKillException,req={0},exceptionInfo={1}".format(req, exceptionInfo))
    pass

# 自定义的结果回调函数
def onKillResult(req, result):
    print("onKillResult", req, result)
    pass

# 统一处理结果
# 统一处理异常
def handleResultAndException():
    # 创建3容量的线程池对象
    myPool = threadpool.ThreadPool(3)
    # def makeRequests(callable_, args_list, callback=None,exc_callback=_handle_thread_exception)
    requests = threadpool.makeRequests(

        # 工作线程所执行的函数
        killWithException,

        ["约汉", "接客", "史密斯", "如花", "秋香"],

        # 统一的结果回调
        callback=onKillResult,

        # 定义统一的异常处理回调函数
        exc_callback=handleKillException
    )
    # 向线程池对象中仍线程请求
    for req in requests:
        myPool.putRequest(req)

    # 阻塞等待池中的线程请求执行完毕
    myPool.wait()


if __name__ == "__main__":
    simpleRequestInPool()
    # complexRequestInPool()
    # handleResultAndException()

    print("main over")
