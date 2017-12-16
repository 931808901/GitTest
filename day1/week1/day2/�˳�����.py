#coding=utf-8
import re
s='-11+4'
# print(re.search('[0-9]+[\*\/][-]?[0-9]+', s).group())
print(re.search("[0-9]{1,}[.]?[0-9]*",s).group())
a=1
b=float(a)
print(type(b))