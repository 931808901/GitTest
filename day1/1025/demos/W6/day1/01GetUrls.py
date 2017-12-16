#! C:\Python36\python.exe
# coding:utf-8
'''
爬取网易主页上的所有子链接
'''
import re

import requests

# <a href="http://home.163.com/">美女海龟辞去高薪工作 回乡改造的旧旅馆美炸了</a>
reUrl = "<a .*href=\"(http.+?)\".*>"
reUrl = re.compile(reUrl)

def printList(mlist):
    for item in mlist:
        print(item)

if __name__ == "__main__":
    html = requests.get("http://www.163.com").text
    # print(html)

    retList = reUrl.findall(html)
    printList(retList)

    print("main over")