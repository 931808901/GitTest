#! C:\Python36\python.exe
'''
正则修饰符
'''
import re

if __name__ == "__main__":
    print(re.match(r"\w+", "你妹"))
    print(re.match(r"\w+", "你妹", flags=re.A))  # 表达式作用于ASCII字符

    print(re.match(r"abc", "ABC"))
    print(re.match(r"abc", "ABC", flags=re.I))  # 表达式不区分大小写

    print(re.match(r"\w+abc", "你妹ABC"))
    print(re.match(r"\w+abc", "你妹ABC", flags=re.U | re.I))  # 表达式作用于Unicode字符&不区分大小写
