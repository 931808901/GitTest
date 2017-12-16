#! C:\Python36\python.exe
# coding:utf-8
'''
冷战死锁
'''
import threading

import time

hFace = threading.Lock()
class Husband(threading.Thread):
    def run(self):
        if hFace.acquire():
            time.sleep(1)

            # 如果老婆先道歉
            print("妻子必须先道歉!")
            if wFace.acquire(timeout=-1):
                if wSorry:
                    print("妻子已道歉")
                    wFace.release()
                    hFace.release()
                    print("Husband：sorry too!")
                else:
                    print("妻子已回娘家")
                    wFace.release()
                    hFace.release()
                    print("Husband：对不起我错了!")

wFace = threading.Lock()
wSorry = False
class Wife(threading.Thread):
    def run(self):
        if wFace.acquire():
            time.sleep(1)

            # 如果丈夫先道歉
            print("丈夫必须先道歉!")
            if hFace.acquire(timeout=5):
                print("丈夫已道歉")
                hFace.release()
                wFace.release()
                print("Wife：sorry too!")

            # 5秒等不来丈夫的道歉，执行PLAN-B
            else:
                print("妈蛋不过了")
                wFace.release()

if __name__ == "__main__":

    Husband().start()
    Wife().start()

    print("main over")