#! C:\Python36\python.exe
# coding:utf-8
'''
线程同步和异步
'''
import threading

import time


def func(name):
    for i in range(10):
        print(name+":",i)
        time.sleep(0.5)

# 5条线程并发执行（异步执行）
def threadAsync():
    for i in range(5):
        threading.Thread(target=func, args=("小分队" + str(i),)).start()


if __name__ == "__main__":
    # threadAsync()
    for i in range(5):
        t = threading.Thread(target=func, args=("小分队" + str(i),))
        t.start()

        # 参加参加，排队排队（劳资没执行完，后边的代码（主线程）给劳资等着）
        # 让主线程【阻塞】等待t执行完毕，才继续向后执行
        t.join()#折行代码是【阻塞】的
        print("-----下一位-----")

    print("main over")