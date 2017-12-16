#! C:\Python36\python.exe
'''
高频特殊字符
[],^,$,[^re],.,re*,re+,\w,\W,\d,\D,\s,\S,re{n},re{n,},re{n,m},|,()
模拟手机、身份证号、网址、邮箱
'''
import re


def func():
    pass


# 模拟手机号匹配
def mimePhone():
    # 我的手机号
    phonePattern = "1[3578]\d{9}"
    resobj = re.match(phonePattern, "13912345678")
    resobj = re.match(phonePattern, "14912345678")
    resobj = re.match(phonePattern, "1399123456")
    print(resobj)


# 我的身份证号
def mimeID():
    # phonePattern = "[^0]\d{16}[\dX]"
    phonePattern = "[^0]\d{5}-((19)|(20))\d{2}-((0[1-9])|(1[0-2]))-((0[1-9])|(1[0-9])|(2[0-9])|(3[0-1]))-\d{3}[\dX]"
    phonePattern = "[^0]\d{5}((19)|(20))\d{2}((0[1-9])|(1[0-2]))((0[1-9])|(1[0-9])|(2[0-9])|(3[0-1]))\d{3}[\dX]"
    resobj = re.match(phonePattern, "123456789012345678")
    resobj = re.match(phonePattern, "12345678901234567X")
    resobj = re.match(phonePattern, "02345678901234567X")
    resobj = re.match(phonePattern, "1234567890124567X")
    resobj = re.match(phonePattern, "123456-7890-1245-678X")
    resobj = re.match(phonePattern, "123456-1999-12-31-678X")
    resobj = re.match(phonePattern, "12345619991231678X")
    print(resobj)


# 我的网址
def mimeUrl():
    phonePattern = "http(s?)://[^\^@~\*]*$"  # 我们的逻辑是：http(s)://跟任意多个【非^@~*】
    resobj = re.match(phonePattern, "http://abcd12345.com")
    resobj = re.match(phonePattern, "http://abcd12345@.com")
    resobj = re.match(phonePattern, "http://abcd12345^.com")
    resobj = re.match(phonePattern, "http://abcd12345~.com")
    resobj = re.match(phonePattern, "http://abcd12345*.com")
    print(resobj)


# 我的邮箱
def mimeMailbox():
    # phonePattern = "^[a-zA-Z0-9][\w]*@[\w]*\.[\w\.]*$"
    phonePattern = "^[a-zA-Z0-9][a-zA-Z0-9_]*@[a-zA-Z0-9_]*\.[a-zA-Z0-9_\.]*$"  #
    resobj = re.match(phonePattern, "12345678@qq.com")
    resobj = re.match(phonePattern, "_12345678@qq.com")
    resobj = re.match(phonePattern, "12345678@qqcom")
    resobj = re.match(phonePattern, "12345你妹678@qq.com")
    print(resobj)


if __name__ == "__main__":
    # mimePhone()
    # mimeID()
    # mimeUrl()
    # mimeMailbox()

    print("main over")
