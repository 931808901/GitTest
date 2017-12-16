#! C:\Python36\python.exe
# coding:utf-8
'''
创建线程
'''
import _thread
import threading

import time

# 子线程所执行的任务函数
# 会与主线程并发执行
def downloadMovie(url,name="代码痴汉",language="C"):
    threadName = threading.current_thread().getName()
    threadId = threading.current_thread().ident

    print("args:",url,name,language)
    print("%d/%s:您的资源：%s正在下载..."%(threadId,threadName,url))
    for i in range(5):
        print(str(threadId)+"/",threadName+":",i)
        time.sleep(1)
    print("%d/%s:下载完成！快来看吧！"%(threadId,threadName))
    pass

# 使用_thread.start_new_thread()开辟守护线程
def startNewThread():
    # 开辟一条子线程，去执行下载任务downloadMovie()，函数参数是"http://www.daoguojiaoyu.com/good.avi"
    _thread.start_new_thread(downloadMovie, ("http://www.daoguojiaoyu.com/good.avi",))
    # 主线程的业务逻辑（会与子线程并发执行）
    mainTid = threading.current_thread().ident
    print("%d/%s:main fuck" % (mainTid, threading.current_thread().getName()))
    time.sleep(1)
    print("%d/%s:main shit" % (mainTid, threading.current_thread().getName()))
    time.sleep(1)
    print("%d/%s:main damn" % (mainTid, threading.current_thread().getName()))
    # 程序结束，所有守护线程殉葬
    while True:
        pass


def createThreadObj():
    # 以创建threading.Thread类所开辟的线程，默认不是【守护线程】
    # threading.Thread(target=downloadMovie,args=("http://www.japan/Python痴汉.avi",)).start()
    # 设置为【守护线程】
    # t = threading.Thread(target=downloadMovie,args=("http://www.japan/Python痴汉.avi",),daemon=True)
    # 配置所有参数
    t = threading.Thread(target=downloadMovie, args=("http://www.japan/Python痴汉.avi",), kwargs={"language": "Python"},
                         daemon=True)
    t.start()
    time.sleep(2)
    print("main over")

# 继承于threading.Thread
# 在run方法中书写线程的业务逻辑
# 通过构造方法传递初始化参数
# 只有run方法是跑在DownloadThread中的
# 其余的哪个线程调用，就跑在哪个线程中
class DownloadThread(threading.Thread):
    def __init__(self,url):
        super(DownloadThread, self).__init__()
        print("我妈调用此方法造我@",threading.current_thread().getName())
        self.url = url

    # run方法干什么，线程就干什么
    def run(self):
        downloadMovie(self.url,language="Python")
    pass


def InheritedThread():
    # mt = DownloadThread(target=downloadMovie, args=("http://www.japan/Python痴汉.avi",), kwargs={"language": "Python"}, daemon=False)
    mt = DownloadThread("http://www.japan/Python痴汉.avi")
    mt.start()
    print("main over")


def threadInfo():
    ct = threading.current_thread()
    tid = ct.ident
    tname = ct.name
    tname2 = ct.getName()
    print(tid, tname, tname2)


def someAPIs():
    for i in range(5):
        threading.Thread(target=downloadMovie, args=("url" + str(i),)).start()
    print("当前活动线程的数量为:%d" % (threading.active_count()))
    print("当前活动线程列表为：", threading.enumerate())


if __name__ == "__main__":
    startNewThread()
    createThreadObj()
    InheritedThread()
    # threadInfo()
    # someAPIs()
    pass