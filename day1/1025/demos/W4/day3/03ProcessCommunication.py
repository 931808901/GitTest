#! C:\Python36\python.exe
# coding:utf-8
'''
·使用Event模拟鼠标点击事件监听
·使用Condition模拟生产消费模型
'''
import multiprocessing

import time
def mouseClick(event):
    pname = multiprocessing.current_process().name
    for i in range(10):
        event.set()
        print("%s:mouseClick"%(pname))
        time.sleep(1)

def osHandleClick(event):
    pname = multiprocessing.current_process().name
    while True:
        event.wait()#阻塞死等
        # ...
        print("%s:osHandleClick"%(pname))
        event.clear()

if __name__ == "__main__":
    # 创建事件对象
    event = multiprocessing.Event()

    # 创建两条进程，一条发送事件，一条监听和处理事件
    multiprocessing.Process(target=mouseClick,args=(event,)).start()
    multiprocessing.Process(target=osHandleClick,args=(event,)).start()

    print("main over")