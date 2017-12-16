#! C:\Python36\python.exe
# coding:utf-8
'''
·在2.0的基础上，将图片的存储名称存储为其实际名称
'''

import re
import threading
from urllib.request import urlretrieve

import requests
import time

from demos.W6.day1.SpiderUtil import printList

# <img src="http://mint-public.nosdn.127.net/mint_1506627137335_53561295.jpg?imageView&amp;thumbnail=250y250" alt="爱我你怂了吗">
reImg = "<img .*src=\"(http.+?)\".*>"
reImg = re.compile(reImg)

# <img src="http://mint_public.nosdn.127.net/mint_1506627137335_53561295.jpg?imageView&amp;thumbnail=250y250" alt="爱我你怂了吗">
reImgName = "/(\w+\.((jpg)|(png)|(gif)|(jpeg)|(bmp)))"
reImgName = re.compile(reImgName)

#
baseUrl = "D:/PyDownload/"


def downloadImg(url, filepath):
    urlretrieve(url, filename=filepath)
    print(url, "下载成功！")


if __name__ == "__main__":
    html = requests.get("http://www.163.com").text
    retList = reImg.findall(html)
    printList(retList)

    tlist = []

    # 并发N条线程
    for i in range(len(retList)):
        url = retList[i]

        # 从url中截取图片名称
        searchObj = reImgName.search(url)
        if searchObj:
            imgName = searchObj.group(1)
        else:
            imgName = "未命名-" + str(int(time.time())) + ".jpg"
        print(imgName)

        # 多线程下载图片
        t = threading.Thread(target=downloadImg, args=(url, baseUrl + imgName))
        t.start()
        tlist.append(t)

    # 主线程等待所有子线程结束
    for t in tlist:
        t.join()

    print("main over")
