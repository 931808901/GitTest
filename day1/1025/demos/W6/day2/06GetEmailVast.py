#! C:\Python36\python.exe
# coding:utf-8
'''
·从一个起始页开始无限爬邮箱，广度优先
·给一个递归深度作为边界
·层次化打印爬取过程，体现子页面层级
'''
from demos.W6.day1.SpiderUtil import getUrls

startUrl = "http://www.baidu.com/s?wd=岛国%20邮箱"

def getEmailVast(startUrl,maxDepth):

    # 向待爬列表中添加地址
    urls = []
    urls.append(startUrl)

    # url=键,层级=值
    depthDict = {}
    depthDict[startUrl] = 1

    # 如果待爬列表中仍有待爬地址
    # 不停地从待爬列表里揪地址爬其邮箱
    while len(urls) > 0:

        # 揪出第一个地址，爬其邮箱
        url = urls.pop(0)
        print("\t" * depthDict[url], depthDict[url], url, "开爬...")

        # 如果当前已经是最大深度了，则不再考虑其子页面
        if depthDict[url] < maxDepth:

            # 得到其子页面
            sons = getUrls(url)
            # 英勇地向宗祠添加下一代香火
            for son in sons:

                # 给儿子赋予层级
                depthDict[son] = depthDict[url] + 1
                urls.append(son)


if __name__ == "__main__":
    getEmailVast(startUrl,3)
    print("main over")
