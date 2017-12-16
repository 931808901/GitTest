#! C:\Python36\python.exe
# coding:utf-8
'''
词频统计器文件夹递归版
求任意文件夹及其所有子文件夹下的文档总词频
'''

'''
·递归：自己调用自己
·必须要有终止条件，否则就是死循环无底洞
·如果递归没有终止条件，会报递归深度越界错误：RecursionError: maximum recursion depth exceeded
'''

import os
import re
from collections import Counter


# 获取任意路径文件（夹）的计数器
# 不管路径是文件还是文件夹
def getFileCounter(filepath):
    counter = Counter()

    # 如果filepath是文件夹，就不断递归兼并
    if os.path.isdir(filepath):

        # 遍历所有子文件（夹）
        sonlist = os.listdir(filepath)
        for son in sonlist:
            son = filepath + "/" + son
            counter += getFileCounter(son)

    # 如果filepath是文本文档，则直接返回自己的计数器
    elif os.path.isfile(filepath) and filepath.endswith(".txt"):
        file = open(filepath,"r",encoding="utf-8")
        text = file.read()
        wordlist = re.findall("[A-Za-z]+",text)
        counter = Counter(wordlist)
        file.close()

    # 如果是非文本文档，啥也不干
    else:
        pass

    # 返回总统计器
    return counter


if __name__ == "__main__":
    dirpath = "../res/"
    counter = getFileCounter(dirpath)
    print(counter.most_common())

    print("main over")
