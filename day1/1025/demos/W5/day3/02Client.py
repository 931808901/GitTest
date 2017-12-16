#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
from socket import socket

host = "127.0.0.1"
port = 1234  # 端口只能是1024-65535

if __name__ == "__main__":
    # 创建客户端socket
    clientSocket = socket()

    # 请求连接（阻塞）
    clientSocket.connect((host, port))

    # 连接成功，与服务端IO
    clientSocket.send("你瞅啥".encode(encoding="utf-8"))
    print("客户端：","你瞅啥")
    reply = clientSocket.recv(1024).decode(encoding="utf-8")
    print("服务端：",type(reply),reply)

    # 主动断开连接
    clientSocket.close()


    print("main over")