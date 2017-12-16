#! C:\Python36\python.exe
# coding:utf-8
'''
匹配、检索、替换
'''
import re

if __name__ == "__main__":
    mPattern = "1[35789][0-9]{9}"#模拟电话号码
    mstr = "我的电话是13912345678"
    # mstr = "13912345678我的电话"
    mstr = "fuck13912345678,shit18612345678,damn188666"
    ret = re.match(mPattern,mstr)#判断大串是否以子串开头
    ret = re.search(mPattern,mstr)#判断大串中有无子串，并返回第一个子串的信息
    ret = re.findall(mPattern,mstr)#从大串中搜索全部子串，以列表返回
    ret = re.sub(mPattern,"【我的亲生儿子】",mstr)#替换大串中的全部子串为【我的亲生儿子】，并返回新的大串
    print(ret)

    print("main over")