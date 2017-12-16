import threading

import threadpool
import time





# 每执行一次kill，就是一条工作线程
# 每次kill的参数用（[whom, price]，{"why":"..."}）
def kill(whom, price, why="凡人皆有一死"):
    tname = threading.current_thread().name
    print("%s正在杀死【%s】,价格是%.2f,原因是【%s】" % (tname, whom, price, why))
    time.sleep(3)
    print("well done！%s" % (tname))

    if whom.isdigit():
        raise RuntimeError("名字不合法")

    if len(whom) < 5:
        return "已成功杀死%s" % (whom)
    else:
        return "失败，%s名字太长记不住" % (whom)

# 处理结果的回调函数
def onKillResult(req,result):
    print("onKillResult,req={0},result={1}".format(req,result))

# 处理异常的回调函数（将来，发生异常，就回调，的函数）
def onKillException(req, exception):
    print("onKillException,req={0},result={1}".format(req, exception))

if __name__ == '__main__':

    # 创建一堆线程（工作请求）
    requests = threadpool.makeRequests(
            kill,
            [
                (["john", 123],{"why":"no reason"}),
                (["jack", 123],{"why":"no reason"}),
                (["smith", 123],{"why":"no reason"}),
                (["1234567", 123],{"why":"no reason"}),
                (["山本五十六", 123],{"why":"no reason"}),
            ],
            callback=onKillResult,
            exc_callback=onKillException
    )

    # 创建指定容量（并发线程数）的池
    myPool = threadpool.ThreadPool(3)

    # 向池中添加线程（WorkRequest工作请求）
    for req in requests:
        myPool.putRequest(req)

    # 阻塞等待池中的线程执行完毕
    myPool.wait()

    pass