# coding:utf-8

from wsgiref.simple_server import make_server
def index():
    return [b'<h1 align="center">welcome</h1>']
def login():
    return [b'<h1 align="center">login</h1>']
# request_url=[('/index',index),('/login',login)]
request_url={'/index':index(),'/login':login()}
# 我们的web应用的名字
def hellowsgi(environ, start_response):
    status = '200 OK'  # HTTP Status
    headers = [('Content-Type', 'text/html')]  # HTTP Headers
    start_response(status, headers)
    print(environ['PATH_INFO'])
    if environ['PATH_INFO'] in request_url.keys():
        return request_url[environ['PATH_INFO']]
    else:
        return [b'<h1 align="center">404</h1>']
    # for url in request_url:
    #     if url[0] == environ ['PATH_INFO']:
    #         return url[1]()
    # return [b'<h1 align="center">404</h1>']


if __name__ == '__main__':
    httpd = make_server('', 8000, hellowsgi)
    print("Serving HTTP on port 8000...")
    # 开启服务
    httpd.serve_forever()