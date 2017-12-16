#! C:\Python36\python.exe
# coding:utf-8
'''
·从一个起始页开始无限爬邮箱，深度优先
·给一个递归深度作为边界
·层次化打印爬取过程，体现子页面层级
'''
from demos.W6.day1.SpiderUtil import getUrls, printList

# url=键,层级=值
depthDict = {}

startUrl = "http://www.baidu.com/s?wd=岛国%20邮箱"
depthDict[startUrl] = 1


# 深度爬邮箱
def getEmailDeep(url, maxDepth):
    # 把自己的邮箱爬了
    print("\t" * depthDict[url], depthDict[url], url, "开爬...")

    # 递归终止条件（层级已满）
    if depthDict[url] >= maxDepth:
        return

    # 打儿子的名字
    sons = getUrls(url)
    for son in sons:

        # 这个son已经当过祖宗了,无视之，看下一个son
        try:
            depthDict[son]
            continue
        except:
            pass

        # 赋予儿子层级
        depthDict[son] = depthDict[url] + 1

        # 对每个儿子递归
        ret = getEmailDeep(son, maxDepth)

    return


if __name__ == "__main__":
    getEmailDeep(startUrl, 4)
    print("main over")
