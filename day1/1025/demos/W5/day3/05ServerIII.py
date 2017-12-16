#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import threading
from socket import socket

import time

host = "127.0.0.1"
port = 1234  # 端口只能是1024-65535


# 与指定的客户端愉快地IO
def ioWithClient(clientSocket,cleintAddress):
    # 与客户端socket进行IO（recv/send）
    while True:
        data = clientSocket.recv(1024).decode(encoding="utf-8")
        print("客户端%s："%(cleintAddress[1]), data)

        msg = "自动回复：%s" % (data)
        clientSocket.send(msg.encode(encoding="utf-8"))
        print("服务端：", msg)

        # 如果客户端说fuck off，断开与他的连接！
        if data == "fuck off":
            print("已断开与客户端的连接")
            break

    # 断开连接
    clientSocket.close()


if __name__ == "__main__":
    # 创建socket对象
    serverSocket = socket()

    # 绑定到端口
    serverSocket.bind((host, port))

    # 监听连接
    serverSocket.listen(100)  # 最大允许100个待连接客户端（100个以后的客户端将被拒绝）
    print("等待客户端连接...")

    while True:
        # 接受客户端socket（阻塞）
        clientSocket, cleintAddress = serverSocket.accept()
        print("成功接入:",cleintAddress)

        threading.Thread(target=ioWithClient,args=(clientSocket,cleintAddress)).start()

    print("main over")
    time.sleep(1)
