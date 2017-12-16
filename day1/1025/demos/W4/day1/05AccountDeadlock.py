#! C:\Python36\python.exe
# coding:utf-8
'''
案例：账户死锁
'''
import threading
from threading import Thread

import time


class BankBook(Thread):
    def __init__(self,account):
        super(BankBook, self).__init__()
        self.account = account

    def run(self):
        if self.account.acquire():
            print("存折正在办业务...")
            time.sleep(5)
            print("存折业务完毕")
            # self.account.release()

class BankCard(Thread):
    def __init__(self,account):
        super(BankCard, self).__init__()
        self.account = account

    def run(self):
        # 只愿意阻塞等待3秒
        if self.account.acquire(timeout=3):
            print("银行卡正在办业务...")
            time.sleep(5)
            print("银行卡业务完毕")
            self.account.release()

        # 等待超时，执行Plan-B
        else:
            print("无法获取银行卡账户信息，请稍后再试！")
            pass

if __name__ == "__main__":
    account = threading.Lock()
    BankBook(account).start()
    BankCard(account).start()
    print("main over")