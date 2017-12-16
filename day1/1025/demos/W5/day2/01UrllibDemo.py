#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
from urllib import request
from urllib.request import Request, urlretrieve


def helloUrllibRequest():
    # 使用urllib类库下的request模块发起http请求，得到响应对象
    resp = request.urlopen("http://www.baidu.com")
    print(type(resp))  # <class 'http.client.HTTPResponse'>
    # 从响应中读取字节，进而解码为字符（html）
    html = resp.read().decode("utf-8")
    print(html)


def getWithArgs():
    resp = request.urlopen("https://www.httpbin.org/get?name=zhangsan&age=20")
    html = resp.read().decode()
    print(html)


def getWithHeaders():
    mReuqst = Request("https://www.httpbin.org/get?name=zhangsan&age=20", headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.2595.400 QQBrowser/9.6.10872.400"})
    resp = request.urlopen(mReuqst)
    html = resp.read().decode("gbk")
    print(html)


def downloadFile():
    ret = request.urlretrieve(
        "https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1508842526632&di=69a58fc62ec20c8aa758c93673ae4bf7&imgtype=0&src=http%3A%2F%2Fk.zol-img.com.cn%2Fdcbbs%2F13371%2Fa13370600_01000.jpg",
        "./gfAndDogs.jpg")
    print(ret)
    print("下载成功!")


if __name__ == "__main__":
    helloUrllibRequest()
    # getWithArgs()
    # getWithHeaders()
    # downloadFile()

    print("main over")