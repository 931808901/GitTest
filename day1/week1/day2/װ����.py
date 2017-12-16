# -*- coding:utf-8 -*-
import time
def timer(func):
    def deco(*args,**kwargs):
        start_time=time.time()
        func(*args,**kwargs)
        stop_time=time.time()
        print('the func run time is %s'%(stop_time-start_time))
    return deco
@timer
def test1(name):
    time.sleep(1)
    print ('in the test1',name)
test1('wang')
