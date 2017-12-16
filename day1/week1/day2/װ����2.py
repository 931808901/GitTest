# -*- coding:utf-8 -*-
import  time
user,passwd='zhang','123456'
def auth(auth_type):
    print ('auth func:',auth_type)
    def outer_wrapper(func):
        def wrapper(*args,**kwargs):
            print ('wrapper func args:', args,kwargs)
            if auth_type=='local':
                username=input('userName:')
                password=input('password:')
                if user==username and passwd==password:
                    print ('local验证成功')
                    res=func(*args,**kwargs)
                    print ('--------after auth-------')
                    return res
                else:
                    exit('验证失败，程序退出')
            elif auth_type=='ldap':
                username=input('userName:')
                password=input('password:')
                if user==username and passwd==password:
                    print ('ldap验证成功')
                    res=func(*args,**kwargs)
                    print ('---after bbs------')
                    return res
                else:
                    exit(   )
        return wrapper
    return outer_wrapper
def index():
    print('welcome to index page')

@auth(auth_type='local')
def home():
    print ('welcome to home page')
    return 'from home'
@auth(auth_type='ldap')
def bbs():
    print ('welcome to bbs page')
    return 'from bbs page'
print (home())
print (bbs())