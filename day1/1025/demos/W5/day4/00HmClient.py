#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import threading
from socket import socket

from os import system

import sys

import time

host = "127.0.0.1"
port = 1234

# 发送消息线程执行此方法
def sendOutput():

    # 源源不断地发送
    while True:
        try:
            msg = input("请输入：")
            clientSocket.send(msg.encode("utf-8"))
            print("客户端：%s" % (msg))

        # 如果服务端已断线，则结束发送线程
        except ConnectionResetError:
            print("服务端已断开连")
            break

# 接收消息线程执行此方法
def recvInput():

    # 源源不断地接收消息
    while True:
        try:
            reply = clientSocket.recv(1024).decode("utf-8")
            print("服务端：%s" % (reply))

        # 如果服务端已断线，则结束消息接收线程
        except ConnectionResetError:
            print("服务端已断开连")
            break


if __name__ == "__main__":

    # 创建socket对象、连接服务端
    clientSocket = socket()
    clientSocket.connect((host,port))

    # 收发消息都在独立的线程中进行
    threading.Thread(target=sendOutput).start()
    threading.Thread(target=recvInput).start()

    # clientSocket.close()
    print("main over")
    time.sleep(10)