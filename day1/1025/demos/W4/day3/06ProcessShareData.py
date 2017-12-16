#! C:\Python36\python.exe
# coding:utf-8
'''
·在两个子进程间共享一个浮点数、一个整数数组
·在A进程改变数据的值，并通知B进程
·在B进程中读取数据的值
-----
·在两个子进程间共享一个字典和一个列表
·A进程改变其值并通知B进程读取
·注意全程不能释放multiprocessing.Manager()
-----
·在两个子进程间共享一个队列
·A进程向队列中放入元素通知B进程读取
·注意处理Full和Empty异常
-----
·在两个子进程间共享一个单工管道
·A进程向管道中放入数据并通知B进程读取
·注意处理OsError（管道已关闭）
'''
import multiprocessing
import queue

import time


def writeValueAndArray(d, sValue, sArray, event):
    d = 34
    sValue.value = 456.5
    sArray[0] = 9999

    event.set()
    pass


def readValueAndArray(d, sValue, sArray, event):
    event.wait()
    print(d, sValue.value, sArray[0])
    pass


def shareValueAndArray():
    d = 12
    sValue = multiprocessing.Value("d", 123.5)
    sArray = multiprocessing.Array("i", [1, 2, 3, 4, 5])

    multiprocessing.Process(target=writeValueAndArray, args=(d, sValue, sArray, event)).start()
    multiprocessing.Process(target=readValueAndArray, args=(d, sValue, sArray, event)).start()


def writeContainer(mlist, mdict, event):
    mlist[0] = "damn"
    mlist.append("shit")
    mdict["name"] = "宇宙非正常人类研究中心"
    event.set()


def readContainer(mlist, mdict, event):
    event.wait()
    print(mlist)
    print(mdict)


event = multiprocessing.Event()


def shareContainer():
    with multiprocessing.Manager() as pm:
        # 普通的容器无法共享
        mlist = ["fuck", 123]

        # 通过pm构造共享的容器
        mlist = pm.list()
        mdict = pm.dict()
        mlist += ["fuck", 123]
        mdict["name"] = "1702"

        # 创建修改进程和读取进程
        wp = multiprocessing.Process(target=writeContainer, args=(mlist, mdict, event))
        rp = multiprocessing.Process(target=readContainer, args=(mlist, mdict, event))
        wp.start()
        rp.start()

        # ！必须阻塞主进程，才能使pm在全程不被释放
        wp.join()
        rp.join()


def writeQueue(mQueue, event):
    try:
        # 永远阻塞，直到能放进去为止
        mQueue.put("fuck", block=True, timeout=None)
        print("put fuck")

        mQueue.put("shit")
        print("put shit")

        # 3秒之后，强行放入（容易造成queue.Full异常）
        mQueue.put("damn", block=False, timeout=3)
        print("put damn")

        # event.set()
    except queue.Full:
        print("丢你妹！队列已满！")
    pass


def readQueue(mQueue, event):
    try:
        while True:
            # 相当于mQueue.get(block=True,timeout=None)，即永远阻塞，直到能拿出元素为止
            # print(mQueue.get())

            print(mQueue.get(block=False,timeout=3))
    except queue.Empty:
        print("拿你妹！队列已空！")
    pass


def shareQueue():
    # 创建共享的队列
    mQueue = multiprocessing.Queue(2)
    # 创建读写进程
    multiprocessing.Process(target=writeQueue, args=(mQueue, event)).start()
    multiprocessing.Process(target=readQueue, args=(mQueue, event)).start()

def pipeSendData(conn,event):
    conn.send("fuck")
    conn.close()
    event.set()

    # 当发送端已关闭时，继续丢入数据，会发生：OSError: handle is closed
    # conn.send("shit")

    # 在单工管道的发送端接收数据，会发生：OSError: connection is write - only
    # print(conn.recv())

    pass
def pipeRecvData(conn,event):
    event.wait()
    print(conn.recv())
    conn.close()

    # 当接收端已关闭时，继续接收数据，会发生：OSError: handle is closed
    # print(conn.recv())

    # 在单工管道的接收端发送数据，会发生：OSError: connection is read-only
    # conn.send("hello")

# 通过单工管道共享数据
def shareDataViaNonduplexPipe():
    myPipe = multiprocessing.Pipe(duplex=False)
    recvConn = myPipe[0]
    sendConn = myPipe[1]
    multiprocessing.Process(target=pipeSendData, args=(sendConn, event)).start()
    multiprocessing.Process(target=pipeRecvData, args=(recvConn, event)).start()

def funcA(conn,event):
    conn.send("im funcA")
    event.set()

    event.wait()
    print(conn.recv())
    pass

def funcB(conn,event):
    event.wait()
    print(conn.recv())

    conn.send("im funcB")
    event.set()
    pass

# 通过双工管道共享数据
def shareDataViaDuplexPipe():
    myPipe = multiprocessing.Pipe(duplex=True)
    multiprocessing.Process(target=funcA, args=(myPipe[0], event)).start()
    multiprocessing.Process(target=funcB, args=(myPipe[1], event)).start()


if __name__ == "__main__":
    # shareValueAndArray()
    # shareContainer()
    # shareQueue()
    # shareDataViaNonduplexPipe()
    # shareDataViaDuplexPipe()

    print("main over")
