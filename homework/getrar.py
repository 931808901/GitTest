#! C:\Python36\python.exe
# coding:utf-8
'''
·爬取网易主页上的所有图片
·所爬图片下载到：D:/PyDownload/
·以序号.jpg命名图片
'''

# <img ...src="..." ...>
import re
import threading
from urllib.request import urlretrieve

import requests


reImg = "<a class=\"download\".*href=\"(http.+?)\".*>"
reImg = re.compile(reImg)


def downloadImg(url, filepath):
    urlretrieve(url, filename=filepath)
    print(url, "下载成功！")


if __name__ == "__main__":
    tlist = []
    for j in range(1,141):
        try:
            html = requests.get("http://www.html5tricks.com/page/"+str(j)).text
            retList = reImg.findall(html)
            # 并发N条线程
            for i in range(len(retList)):
                url = retList[i]
                t = threading.Thread(target=downloadImg,args=(url, "D:/html/" +str(j)+'_'+ str(i) + ".rar"))
                t.start()
                tlist.append(t)
        except:
            pass
    # 主线程等待所有子线程结束
    # for t in tlist:
    #     t.join()

    print("main over")
