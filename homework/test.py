# coding=utf-8
from PIL import Image
import os
#使用第三方库：Pillow
import math
import operator
from functools import reduce
path=u'D:\\html5特效\\特效图片\\'
image1=Image.open(u'D:\\html5特效\\特效图片\\1_0.jpg')
image3=Image.open(u'D:\\html5特效\\特效图片\\1_1.jpg')
files=os.listdir(path)
#把图像对象转换为直方图数据，存在list h1、h2 中
count=0
for i in files:
    try:
        image1=Image.open(path+i)
        h1=image1.histogram()
        for j in files:
            try:
                image3=Image.open(path+j)
                h2=image3.histogram()
                result = math.sqrt(reduce(operator.add,  list(map(lambda a,b: (a-b)**2, h1, h2)))/len(h1) )
                if result==0.0 and i!=j:
                    count+=1
            except:
                pass
    except:
        pass
print(count)
'''
sqrt:计算平方根，reduce函数：前一次调用的结果和sequence的下一个元素传递给operator.add
operator.add(x,y)对应表达式：x+y
这个函数是方差的数学公式：S^2= ∑(X-Y) ^2 / (n-1)
'''
# print(result)
#result的值越大，说明两者的差别越大；如果result=0,则说明两张图一模一样