#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import socket
from urllib import request

import requests


def urllibTimeout():
    try:
        resp = request.urlopen("http://www.sina.com", timeout=0.1)
        print(resp.read().decode("utf-8"))
    except socket.timeout:
        print("超时")
        pass


def requestsTimeout():
    try:
        resp = requests.get("http://www.jd.com", timeout=0.005)
        print(resp.text)
    except requests.exceptions.ReadTimeout:
        print("超时")
    except requests.exceptions.ConnectTimeout:
        print("超时")


if __name__ == "__main__":
    # urllibTimeout()
    requestsTimeout()

    print("main over")