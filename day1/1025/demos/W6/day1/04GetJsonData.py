#! C:\Python36\python.exe
# coding:utf-8
'''
·在今日头条中搜索美女，得到待爬取的美女组图
·捕获其json数据
·分析其json数据
·将组图爬取下载到D:\\PyDownload\\
·创建组图同名的文件夹
·将所有图片下载到对应的组图文件夹下
'''
import json
import os
import re
import threading
from urllib.request import urlretrieve

import requests

from demos.W6.day1.SpiderUtil import downloadImg

# 下载根路径
basePath = "D:\\PyDownload\\"

# 渗透所得的json数据地址
url = "https://www.toutiao.com/search_content/?offset=0&format=json&keyword=%E7%BE%8E%E5%A5%B3&autoload=true&count=20&cur_tab=3"

# 从图片地址中抽取图片名称的正则
# http://p3.pstatp.com/large/3a08000130c5bafc9a52
reImgName = ".+/(\w+)"
reImgName =  re.compile(reImgName)#预编译

if __name__ == "__main__":

    # 发起http请求获取json数据
    mJson = requests.get(url).text

    # 转化为python对象（字典和列表相互嵌套的结构）
    mDict = json.loads(mJson)
    # print(type(mDict))
    # print(mDict)

    # 下载线程容器（以便让主线程等待他们）
    tlist = []

    # 根据json的具体结构解析其数据
    groupList = mDict["data"]
    for groupDict in groupList:

        # 获取所有组图名称
        title = groupDict["title"]
        # print(title)

        # 创建title的同名文件夹
        path = basePath + title + "\\"
        # 如不存在就创建
        if not os.path.exists(path):
            os.mkdir(path)
        print(path,"创建完毕")

        # 下载组图下的图片到对应文件夹
        imgList = groupDict["image_detail"]
        for imgDict in imgList:

            # 获取组图下的所有图片地址
            imgUrl = imgDict["url"]

            # 以imgUrl的最后一段作为图片名称
            imgName = reImgName.search(imgUrl).group(1)+".jpg"

            # 发起多线程异步下载
            t = threading.Thread(target=downloadImg,args=(imgUrl,path+imgName))
            t.start()
            tlist.append(t)

    # 等待所有下载完毕
    for t in tlist:
        t.join()

    # 通知所有子线程已完工
    print("main over")