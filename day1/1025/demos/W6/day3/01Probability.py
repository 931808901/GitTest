#! C:\Python36\python.exe
# coding:utf-8
'''
·同时掷出两只色子，统计同时为1的概率；
·使用样本统计法，而非相关公式；
'''
import random

# 模拟掷两个色子
def throwDice():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    return (a, b)


if __name__ == "__main__":
    print("标准答案：", (1 / 6) * (1 / 6))

    count = 0
    times = 100000
    # 连续掷times次
    for i in range(times):
        ret = throwDice()

        # 统计标的出现的次数
        if ret[0] == ret[1] == 1:
            count += 1

    # 求得概率
    print("统计结果：%d/%d" % (count, times), count / times)
    print("main over")
