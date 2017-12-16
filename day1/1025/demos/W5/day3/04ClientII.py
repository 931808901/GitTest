#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
from socket import socket

import time

host = "127.0.0.1"
port = 1234  # 端口只能是1024-65535

if __name__ == "__main__":
    # 创建客户端socket
    clientSocket = socket()

    # 请求连接（阻塞）
    clientSocket.connect((host, port))

    # 连接成功，与服务端IO
    while True:
        try:
            msg = input("请输入：")
            clientSocket.send(msg.encode(encoding="utf-8"))

            reply = clientSocket.recv(1024).decode(encoding="utf-8")
            print("服务端：",reply)

            if msg == "fuck off":
                print("客户端结束了聊天")
                break

        # 连接异常断开
        except ConnectionAbortedError:
            print("已断开与服务端的连接")
            break

    # 主动断开连接
    clientSocket.close()
    print("main over")
    time.sleep(1)