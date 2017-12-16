#! C:\Python36\python.exe
'''
非高频特殊字符
'''
import re


def func():
    pass


# 单词边界
def s1():
    pattern = r"er\b"
    pattern = r"er\B"
    print(re.search(pattern, "never"))
    print(re.search(pattern, "verb"))


# 其它特殊字符举例
def s2():
    print(re.match("(?i)abc", "ABC"))
    print(re.match("(?i)abc", "AbC"))
    print(re.match("(?i)abc(?#你妹我是注释)", "AbC"))
    print(re.match("a(?=bc)", "abc"))
    print(re.match("a(?=bc)", "a mother fucker"))
    print(re.match("a(?!bc)", "abc"))
    print(re.match("a(?!bc)", "a mother fucker"))
    print(re.search("(?<=bc)a", "bca"))
    print(re.search("(?<=bc)a", "fxa"))
    print(re.search("(?<!bc)a", "bca"))
    print(re.search("(?<!bc)a", "fxa"))


if __name__ == "__main__":
    # s1()
    s2()
