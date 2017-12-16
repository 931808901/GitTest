#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
from urllib.request import urlretrieve

import requests

# 从自己的服务端获取JSON数据
def getJsonFromServer():
    url = "http://localhost/cgi-bin/07GetUserInfo.py?id=1234"
    resp = requests.get(url)
    print(resp.text)


def downloadFileFromServer():
    urlretrieve("http://localhost/imgs/gfs.jpg", "./gfs.jpg")
    print("下载完成")


if __name__ == "__main__":
    # getJsonFromServer()
    # downloadFileFromServer()

    # 访问url得到HTTPResponse对象
    resp = requests.get("http://localhost/imgs/dog.jpg")

    # with一个文件对象的时候，with结束时文件会自动关闭
    with open("./gfs.jpg","wb") as file:
        # 写出小文件，一次性写出
        # file.write(resp.content)

        # 写出大文件，eg：python痴汉.avi
        # 一个缓冲区一个缓冲区地写出
        # HTTPResponse对象可以迭代访问，元素是一小包一小包的字节
        for buffer in resp:
            file.write(buffer)

    print("下载完成")

    print("main over")