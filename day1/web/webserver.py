# coding: utf-8
import socket

#定义处理函数
def handle_request(client):
    # 接收请求
    buf = client.recv(1024)
    #返回信息
    client.send('HTTP/1.1 200 OK\r\n\r\n'.encode('utf-8'))
    client.send('<h1 align="center">hello word</h1>'.encode('utf-8'))

# socket 服务器
def main():
    # 创建socket对象
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    #监听8000端口
    sock.bind(('localhost',8000))
    #最大允许排队的客户端
    sock.listen(5)

    #循环等待客户的链接
    while True:
        #等待用户的链接，默认accept阻塞，当有请求时往下执行
        connection,address = sock.accept()
        #把链接交给处理函数
        handle_request(connection)
        #关闭链接
        connection.close()

if __name__ == '__main__':
    main()

