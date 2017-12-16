#! C:\Python36\python.exe
# coding:utf-8
'''
扩展
'''
import threading

import time

from demos.W6.day1.SpiderUtil import getUrls

urlList = []
depthDict = {}


def addUrls(url):
    sons = getUrls(url)
    for son in sons:
        depthDict[son] = depthDict[url] + 1
        urlList.append(son)


if __name__ == "__main__":

    # 丢入起始页到待爬列表
    startUrl = "http://www.baidu.com/s?wd=岛国%20邮箱"
    depthDict[startUrl] = 1
    urlList.append(startUrl)

    # 是否可以驾鹤西去了，默认不可以
    iCanToHellNow = False

    # 源源不断地从待爬列表中揪地址爬其邮箱，揪完为止
    while len(urlList) > 0 or threading.active_count() > 1:

        # 没得地址可揪，一直等到有地址可揪
        while len(urlList) == 0:

            # 待爬列表也空了，工作线程也没了，就可以驾鹤西去了
            if threading.active_count() == 1:
                iCanToHellNow = True
                break
            else:
                pass

        if iCanToHellNow:
            break

        # 揪一个，爬邮箱
        url = urlList.pop(0)
        urlDepth = depthDict[url]
        print("\t" * urlDepth, urlDepth, url, "开爬...")

        # 如果层级未满的情况下，揪出来的地址向待爬列表中生孩子
        if urlDepth < 3:
            t = threading.Thread(target=addUrls, args=(url,))
            t.start()

        # 每次添加一批工作线程，小睡一会会，让工作线程active起来
        time.sleep(0.01)

    print("main over")
