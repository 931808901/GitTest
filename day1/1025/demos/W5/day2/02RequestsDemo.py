#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import json

import requests


def helloRequests():
    resp = requests.get("https://www.httpbin.org/get?name=张三&age=20")
    # requests.Response对象的content属性是字节类型
    # mBytes = resp.content
    # html = mBytes.decode("utf-8")
    html = resp.text
    print(html)


def getWithArgs():
    params = {"name": "张三", "age": 20}
    resp = requests.get("https://www.httpbin.org/get", params=params)
    print(resp.text)


def postForm():
    data = {"name": "张三", "age": 20}
    resp = requests.post("https://www.httpbin.org/post", data=data)
    print(resp.text)


def postJson():
    data = {"name": "张三", "age": 20}
    resp = requests.post("https://www.httpbin.org/post", json=json.dumps(data))
    print(resp.text)


def downloadFile():
    resp = requests.get(
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1509435166&di=9211d3f44a0da6cf3f69431154cbb3c7&imgtype=jpg&er=1&src=http%3A%2F%2Fc.hiphotos.baidu.com%2Fzhidao%2Fpic%2Fitem%2F7dd98d1001e93901d31632ce7bec54e736d1962e.jpg")
    mBytes = resp.content
    with open("./dog.jpg", "wb") as file:
        file.write(mBytes)
        file.close()
    print("下载成功！")


def postFile():
    file = open("./dog.jpg", "rb")
    resp = requests.post("https://www.httpbin.org/post", files={"file": file})
    print(resp.text)


if __name__ == "__main__":
    # helloRequests()
    # getWithArgs()
    # downloadFile()

    # postForm()
    # postJson()
    # postFile()

    print("main over")