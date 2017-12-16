#! C:\Python36\python.exe
# coding:utf-8
'''
多线程版的TCPServer，为每个客户端Socket创建一个独立的线程
'''
from socketserver import ThreadingTCPServer, StreamRequestHandler, BaseRequestHandler

host = "127.0.0.1"
port = 1234  # 端口只能是1024-65535

# 自定义的客户端业务逻辑处理类
class MyRequestHandler(BaseRequestHandler):

    # 结束时回调
    def finish(self):
        print("finish")
        "客户端%s断开连接" % (self.client_address[1])
        super(MyRequestHandler, self).finish()

    # 启动时回调
    def setup(self):
        print("setup")
        print("客户端%s连接成功"%(self.client_address[1]))
        super(MyRequestHandler, self).setup()

    # 处理业务逻辑
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


if __name__ == "__main__":
    # 创建ThreadingTCPServer对象，绑定服务端地址和【业务处理器类】
    server = ThreadingTCPServer((host, port),MyRequestHandler)

    # 永远服务
    server.serve_forever()

    print("main over")
