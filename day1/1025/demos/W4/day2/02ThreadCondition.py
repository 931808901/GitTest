#! C:\Python36\python.exe
# coding:utf-8
'''
线程通信-Condition实现双向线程通信
生产者和消费者模型：
生产者线程生产出产品后通知消费者线程来消费，自己原地等候消费者的生产通知
消费者消费掉产品，通知生产者生产，自己原地等候生产者的消费通知
'''
import threading

# 产品封装类
import time


class Product:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "<Product:%s>" % (self.name)


# 生产者线程
class Producer(threading.Thread):
    def __init__(self, condition, shop):
        super().__init__()
        self.condition = condition
        self.shop = shop

    def run(self):
        # 源源不断地抢信物，并生产
        while True:
            with condition:
                # 造出产品，放入商店
                p = Product(time.ctime())
                shop.append(p)
                print("生产者生产了", p)
                time.sleep(1)

                # 通知正在wait的人（消费者）消费
                # condition.notify()
                condition.notify_all()

                # 自己交出信物，原地等候通知
                condition.wait()  # 阻塞

        print("生产者over")


# 消费者线程
class Consumer(threading.Thread):
    def __init__(self, name, condition, shop):
        super().__init__()
        self.name = name
        self.condition = condition
        self.shop = shop

    def run(self):
        # 循环抢信物并消费
        while True:
            with condition:
                try:
                    # 消费商店中的产品
                    p = shop.pop(0)
                    print("%s消费了" % (self.name), p)

                    # 通知正在wait的线程（通知生产者生产）
                    condition.notify()
                except:
                    print("%s卵都没吃到"%(self.name))

                time.sleep(0.5)

                # 交出信物，等候下一次消费通知
                condition.wait()  # 阻塞等待被notify

        print("Consumer over")


if __name__ == "__main__":
    # 创建线程双向通信信物
    condition = threading.Condition()
    shop = []  # 模拟商店

    # 生产者线程、消费者线程跑起
    Producer(condition, shop).start()
    Consumer("foo", condition, shop).start()
    Consumer("bas", condition, shop).start()
    Consumer("pig", condition, shop).start()

    print("main over")
