#! C:\Python36\python.exe
# coding:utf-8
'''
·并发访问5个网站
·哪个网站阻塞就自动让出执行权
·谁最早获得结果（结束阻塞）就先打印谁的结果
*使用gevent的睡眠机制+monkey.patch_all()，联合网络访问函数，实现网络的非阻塞IO访问
'''
import gevent
import requests
from gevent import monkey


def getHtml(order,url):
    print("No.%d 正在访问%s..."%(order,url))
    resp = requests.get(url)#阻塞
    html = resp.text
    print("No.%d：%s访问成功，数据长度为%d"%(order,url,len(html)))


def main():
    # 阻塞IO（访问网络）转换为非阻塞IO
    monkey.patch_all()
    gevent.joinall([
        gevent.spawn(getHtml, 1, "http://www.youku.com"),
        gevent.spawn(getHtml, 2, "http://www.163.com"),
        gevent.spawn(getHtml, 3, "http://www.sohu.com"),
        gevent.spawn(getHtml, 4, "http://www.sina.com"),
        gevent.spawn(getHtml, 5, "http://www.qq.com"),
        gevent.spawn(getHtml, 6, "http://www.google.com"),
        gevent.spawn(getHtml, 7, "http://www.iqiyi.com"),
    ])


if __name__ == "__main__":
    main()
    print("main over")