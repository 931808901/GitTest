# coding:utf-8

from wsgiref.simple_server import make_server
from jinja2 import Template
from datetime import datetime

# 自定义处理url的函数
def index():
    f = open('html/index.html','r')
    data = f.read()
    f.close()

    # 创建template实例
    template = Template(data)
    # 用特定的数据去渲染模板
    result = template.render(
        name = 'john',
        age = '18',
        time = str(datetime.now()),
        user_list = ['zhangsan', 'lisi', 'michael'],
        num = 1
    )
    return result.encode('utf-8')


def login():
    f = open('html/login.html')
    data = f.read()
    f.close()

    return data


# 自定义路由
url_list = [
    ('/index/', index),
    ('/login/', login),
]


# 定义一个helloworld的app
def hello_world_app(environ, start_response):
    status = '200 OK'
    headers = [('Content-Type', 'text/html')]
    start_response(status, headers)
    request_url = environ['PATH_INFO']
    print (request_url)
    for url in url_list:
        if request_url == url[0]:
            print (url)
            # 说明url匹配成功
            # 执行对应的函数
            return url[1]()
    else:
        return '<h1>404</h1>'



# 使用wsgiref封装好的函数启动socket服务
httpd = make_server('', 8000, hello_world_app)
print('HTTP Serving...')
# 服务一直运行
httpd.serve_forever()