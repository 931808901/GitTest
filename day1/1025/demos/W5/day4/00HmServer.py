#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import threading
from socket import socket

host = "127.0.0.1"
port = 1234
clientDict = {}

# 全局发送消息方法（目标客户端由消息内容指定）
def sendOutput():

    # 源源不断地发送
    while True:
        msg = input("请输入childPort:msg")

        # 从消息中剥离出客户端端口
        clientPort = msg.split(":")[0]
        try:

            # 根据端口从全局客户端字典中拿到对应的客户端socket
            targetSocket = clientDict[clientPort]

            # 对该socket发送消息
            targetSocket.send(msg.encode("utf-8"))
            print("服务端：%s" % (msg))

        # 如果字典中已经将输入的端口socket除名，打印异常信息
        except KeyError:
            print("客户端%s已断开连接" % (clientPort))

# 接收指定客户端消息
def recvInput(clientSocket,clientAddress):

    # 源源不断地接收
    while True:
        try:

            # 接收消息
            msg = clientSocket.recv(1024).decode("utf-8")
            print("客户端%s：%s" % (clientAddress[1], msg))

        # 如果客户端已经断线，就关闭与他的连接，并从全局客户端字典中除名，并结束对他的消息接收
        except ConnectionResetError:
            print("客户端%d已断开连接" % (clientAddress[1]))
            clientSocket.close()
            clientDict.pop(str(clientAddress[1]))
            break


if __name__ == "__main__":

    # 创建socket、绑定端口、设置监听
    serverSocket = socket()
    serverSocket.bind((host, port))
    serverSocket.listen(100)

    # 一条独立的消息发送线程（发送给谁由消息内容来指定）
    threading.Thread(target=sendOutput).start()

    # 源源不断地接入客户端socket
    while True:
        clientSocket, clientAddress = serverSocket.accept()
        # print(type(clientAddress[1]))

        # 将客户端socket保存到全局字典，以便查询和操作
        clientDict[str(clientAddress[1])] = clientSocket

        # 为每个客户端开辟一条独立的消息接收线程
        threading.Thread(target=recvInput, args=(clientSocket, clientAddress)).start()

    print("main over")
    time.sleep(10)
