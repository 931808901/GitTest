#! C:\Python36\python.exe
# coding:utf-8
'''
手机、邮箱、身份证、网址
'''
import re

if __name__ == "__main__":

    # 手机
    mPattern = "1[35789]\d{9}"
    mstr = "fuck"
    mstr = "13988888888ismyphone"

    # 网址
    mPattern = "(https?://)?www\..+"
    mstr = "http://www.baidunimei.com"
    mstr = "https://www.baidunimei.com"
    mstr = "www.baidunimei.com"

    # 邮箱
    mPattern = "([a-z]|\d)([a-z]|\d|_)+@([a-z]|\d)+\.([a-z]|\d)+.*"
    mstr = "12345@qq.com"
    mstr = "12345nimei@qq.com.cn"
    mstr = "12345nimeiqq.com.cn"
    mstr = "12A345nimei@qq.com.cn"
    mstr = "_12345nimei@qq.com.cn"

    # 身份证号
    # mPattern = "123456-1900-01-31-123X"
    mPattern = "[1-9]\d{5}-((19\d{2})|(200\d)|(201[0-7]))-((0[1-9])|(1[012]))-((0[1-9])|([12]\d)|((?<!02-)3[01]))-\d{3}[\dX]"
    mstr = "123456-1949-10-01-6666"
    mstr = "123456-2049-10-01-6666"
    mstr = "123456-1949-10-01-666X"
    mstr = "023456-1949-10-01-666X"
    mstr = "123456-1949-02-30-666X"

    ret = re.match(mPattern,mstr)
    print(ret)

    print("main over")