#! C:\Python36\python.exe
# coding:utf-8
'''
·使用gevent的睡眠机制，联合四个协程函数，打印一首小诗(gevent.sleep())
·使用gevent的睡眠机制，联合四个写成函数，讲述浏览器的故事
----------
@笔记
·gevent一旦阻塞/睡眠，就会自动让出CPU执行权
·执行权会优先传递给不阻塞/不睡眠或阻塞睡眠时间较短的协程函数
·对于阻塞/睡眠时间相同的协程函数，按照joinall的顺序分配CPU执行权
'''
import gevent


def geventFunc1():
    gevent.sleep(0)
    print("红军不怕远征难")
    gevent.sleep(5)  # 模拟阻塞

    print("金沙水拍云崖暖")


def geventFunc2():
    gevent.sleep(1)
    print("万水千山只等闲")
    gevent.sleep(5)  # 模拟阻塞

    print("大渡桥横铁索寒")


def geventFunc3():
    gevent.sleep(2)
    print("五岭逶迤腾细浪")
    gevent.sleep(5)  # 模拟阻塞

    print("更喜岷山千里雪")


def geventFunc4():
    gevent.sleep(3)
    print("乌蒙磅礴走泥丸")
    gevent.sleep(5)  # 模拟阻塞

    print("三军过后尽开颜")


def helloGevent():
    # 没有阻塞/睡眠的时候，按顺序执行
    gevent.joinall([
        gevent.spawn(geventFunc1),
        gevent.spawn(geventFunc3),
        gevent.spawn(geventFunc2),
        gevent.spawn(geventFunc4),
    ])


def chrome(request):
    gevent.sleep(1)
    print("chrome:", questionDict[request])


def firefox(request):
    gevent.sleep(1)
    print("firefox:", questionDict[request])


def safari(request):
    gevent.sleep(1)
    print("safari:", questionDict[request])


def ie(request):
    gevent.sleep(9)
    print("ie:", questionDict[request])


questionDict = {
    "我们是什么？": "浏览器",
    "我们要什么？": "速度",
    "什么时候要？": "现在",
}


def browserStory():
    questions = list(questionDict.keys())
    for i in range(len(questions)):
        question = questions[i]
        print(question)
        gevent.joinall([
            gevent.spawn(ie, question),
            gevent.spawn(firefox, question),
            gevent.spawn(safari, question),
            gevent.spawn(chrome, question),
        ], timeout=3)


if __name__ == "__main__":
    # helloGevent()
    # browserStory()

    print("main over")
