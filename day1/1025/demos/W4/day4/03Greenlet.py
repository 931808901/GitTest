#! C:\Python36\python.exe
# coding:utf-8
'''
·使用greenlet，联合两个协程函数，打印一首小诗（gr.switch()）
'''
from greenlet import greenlet

import time


def greenFunc1():
    print("开门走进卫生间")
    time.sleep(1)

    # 让出CPU执行权给greenFunc2
    gr2.switch()

    print("飞流直下三千尺")
    time.sleep(1)

    # 让出CPU执行权给greenFunc2
    gr2.switch()

def greenFunc2():
    print("一看拖把放旁边")
    time.sleep(1)

    # 让出CPU执行权给greenFunc1
    gr1.switch()

    print("疑是银河落九天")
    time.sleep(1)


gr1 = greenlet(greenFunc1)
gr2 = greenlet(greenFunc2)
if __name__ == "__main__":
    gr1.switch()

    print("main over")