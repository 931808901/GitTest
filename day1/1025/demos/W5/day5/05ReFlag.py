#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import re

if __name__ == "__main__":
    # ret1 = re.match("\w+","Aa123_你妹")
    # ret2 = re.match("\w+","Aa123_你妹",flags=re.A)

    # ret1 = re.match("ABC","ABC你妹")
    # ret2 = re.match("ABC","abc你妹",flags=re.I)

    ret1 = re.match("\w+","Aa123_你妹")
    ret2 = re.match("abc\w+","Abc123_你妹",flags=re.I|re.U)

    print(ret1)
    print(ret2)

    print("main over")