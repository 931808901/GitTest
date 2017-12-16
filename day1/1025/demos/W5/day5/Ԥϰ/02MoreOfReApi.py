#! C:\Python36\python.exe
'''
更多的正则API
'''
import re


def func():
    pass


# 结果子串及其位置
def groupAndSpan():
    pattern = "[Pp]ython"
    str1 = "python一出谁与争锋"
    print(re.match(pattern, str1).group())  # 满足样式的子串python
    print(re.match(pattern, str1).span())  # 子串出现的位置(0, 6)


# 样式分组，分组子串，分组子串位置
def groupAndSpanWithGroupIndex():
    # 包含分组的正则样式
    pattern = "(.*)( are )(.*)"
    str1 = "Cats are smarter than dogs"
    print(re.match(pattern, str1))
    # 全部子串
    print(re.match(pattern, str1).group())
    # 样式中【第n组对应的子串】
    print(re.match(pattern, str1).group(1))
    print(re.match(pattern, str1).group(2))
    print(re.match(pattern, str1).group(3))
    # 全部子串对应的位置跨度
    print(re.match(pattern, str1).span())
    # 样式中【第n组对应的子串】对应的位置
    print(re.match(pattern, str1).span(1))
    print(re.match(pattern, str1).span(2))
    print(re.match(pattern, str1).span(3))


# 检索第一个子串出现的位置
def searchSpan():
    pattern = "[Pp]ython"
    str1 = "一出python，谁与争锋"
    print(re.search(pattern, str1).span())


if __name__ == "__main__":
    # groupAndSpan()
    # groupAndSpanWithGroupIndex()
    # searchSpan()

    print("main over")
