#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
from socket import socket

host = "127.0.0.1"
port = 1234  # 端口只能是1024-65535

if __name__ == "__main__":
    # 创建socket对象
    serverSocket = socket()

    # 绑定到端口
    serverSocket.bind((host, port))

    # 监听连接（阻塞）
    serverSocket.listen(100)  # 最大允许100个待连接客户端（100个以后的客户端将被拒绝）

    # 接受客户端socket
    clientSocket, cleintAddress = serverSocket.accept()

    # 与客户端socket进行IO（recv/send）
    data = clientSocket.recv(1024).decode(encoding="utf-8")
    print("客户端：",type(data), data)

    clientSocket.send("瞅你咋滴".encode(encoding="utf-8"))
    print("服务端：","瞅你咋滴")

    # 断开连接
    clientSocket.close()
    print("main over")
