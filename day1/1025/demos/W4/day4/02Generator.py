#! C:\Python36\python.exe
# coding:utf-8
'''
1、简易生成器
·基于一个列表创建生成器
·使用next(gen)遍历该生成器（遇见StopIteration结束遍历）
----------
2、斐波那契数列生成器
·求斐波那契数列第N项
·获得N项斐波那契数的生成器
·遍历该生成器
----------
@笔记
·斐波那契数列：0,1,1,2,3,5,8,13...
'''
import time


def myGenerator():
    print("myGenerator start...")

    miterable = ["fuck", "shit", "asshole"]
    for item in miterable:
        print("generate...")
        yield item  # 将item连同CPU执行权一起让给main函数
        # 执行权已被让出
        print("-----hello-----")

    print("myGenerator over!")


def helloGenerator():
    gen = myGenerator()
    print("开始索取元素")
    while True:
        try:
            print("喂来一个")
            print(next(gen))  # 将CPU的执行权给生成器
            print("sleep")
            time.sleep(3)
        except StopIteration:
            print("生成完毕！")
            break


# 求斐波那契数列第N项:0,1,1,2,3,5,8,13...
def getFibonacciNumber(n):
    a = 0
    b = 1

    for i in range(n - 1):
        c = a + b
        a, b = b, c

    return a

# 获得N项斐波那契数的生成器
def getFibonacciGenerator(n=10):
    a = 0
    b = 1
    yield a

    count = 1
    while count < n:
        count += 1
        c = a + b
        a, b = b, c
        yield a


def useFibonacciGenerator():
    fiboGen = getFibonacciGenerator(100)
    # for item in fiboGen:
    #     print(item)
    while True:
        try:
            print(next(fiboGen))
        except StopIteration:
            break


if __name__ == "__main__":
    # helloGenerator()
    print(getFibonacciNumber(10))
    # useFibonacciGenerator()

    print("main over")
