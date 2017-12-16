#! C:\Python36\python.exe
# coding:utf-8
'''
词频统计器
wordlist = re.findall(pattern,text)
counter = Counter(wordlist)
reslist = counter.most_common()
'''

'''
·递归：自己调用自己
·必须要有终止条件，否则就是死循环无底洞
·如果递归没有终止条件，会报递归深度越界错误：RecursionError: maximum recursion depth exceeded
'''

import os
import re
from collections import Counter


# 得到文本文件的计数器
def getFileCounter(filePath):
    file = open(filePath, "r", encoding="utf-8")
    text = file.read()
    # print(text)
    file.close()
    wordlist = re.findall("[A-Za-z]+", text)
    # print(wordlist)
    counter = Counter(wordlist)

    # reslist = counter.most_common()
    # print(reslist)
    return counter


# 获得一个目录下所有一级txt文档的总词频
def getDirDocWordFrequency(dirPath):
    # 遍历一个文件夹，得到所有文本文档
    fileNames = os.listdir(dirPath)
    print(fileNames)
    mlist = []
    for fname in fileNames:
        if fname.endswith(".txt"):
            mlist.append("../res/" + fname)
    print(mlist)
    # 对所有文本文档逐个获取其计数器，形成总计数器
    counter = Counter()
    for fname in mlist:
        counter += getFileCounter(fname)

    # 对所有计数器加总求总词频
    ret = counter.most_common()
    print(ret)
    return ret


if __name__ == "__main__":
    # getDirDocWordFrequency()

    print("main over")
