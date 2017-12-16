#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
from socketserver import TCPServer, BaseRequestHandler

host = "127.0.0.1"
port = 1234  # 端口只能是1024-65535

# 自定义的客户端业务逻辑处理类
class MyRequestHandler(BaseRequestHandler):

    # 每次接入一个客户端请求，就为他创建一个MyRequestHandler的对象
    # request=客户端socket
    # client_address=客户端地址
    # server=服务端TCPServer对象
    def __init__(self, request, client_address, server):
        print("__init__",request, client_address, server)
        super().__init__(request, client_address, server)

    def handle(self):
        print("handle...")
        # 与客户端socket进行IO（recv/send）
        while True:
            data = self.request.recv(1024).decode(encoding="utf-8")
            print("客户端%s：" % (self.client_address[1]), data)

            msg = "自动回复：%s" % (data)
            self.request.send(msg.encode(encoding="utf-8"))
            print("服务端：", msg)

            # 如果客户端说fuck off，断开与他的连接！
            if data == "fuck off":
                print("已断开与客户端的连接")
                break

    # 结束时回调
    def finish(self):
        print("finish")
        self.request.close()
        "客户端%s断开连接" % (self.client_address[1])

    # 预处理
    def setup(self):
        print("setup")
        print("客户端%s连接成功"%(self.client_address[1]))


if __name__ == "__main__":
    # 创建TCPServer对象，绑定地址和【业务处理器类】
    server = TCPServer((host,port),MyRequestHandler)

    # 永远服务
    server.serve_forever()

    print("main over")