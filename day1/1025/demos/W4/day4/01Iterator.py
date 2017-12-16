#! C:\Python36\python.exe
# coding:utf-8
'''
·创建字符串和容器的迭代器
·简易方式遍历迭代器
·使用next(it)遍历迭代器
--------------------
@笔记
·遍历可以重复，迭代只有一轮
'''

if __name__ == "__main__":
    # 可迭代对象
    miterable = "hello"
    miterable = ("fuck","shit","asshole")
    miterable = ["fuck","shit","asshole"]
    miterable = {"fuck","shit","asshole"}
    # 字典迭代出来的结果是键
    miterable = {"姓名":"fuck","喜欢的食物":"shit","人品":"asshole"}

    # 创建其迭代器
    it = iter(miterable)

    # 简易迭代
    # for item in it:
    #     print(item)

    # next迭代：使用next(it)逐个访问下一个元素，直到迭代到队尾
    while True:
        try:
            # 逐个访问下一个元素
            print(next(it))

        # 迭代已到终点
        except StopIteration:
            break

    print("main over")