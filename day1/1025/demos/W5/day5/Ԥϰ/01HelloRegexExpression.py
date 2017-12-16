#! C:\Python36\python.exe
'''
正则表达式API
'''
import re


def func():
    pass


# 匹配：判断字符串是否以【正则表达式描述的样式pattern】开头
def reMatch():
    pattern = "[Pp]ython"
    str1 = "天不生python，世间万古如长夜"
    str2 = "python一出谁与争疯"
    str3 = "Python一出谁与争疯"
    resobj = re.match(pattern, str1)
    resobj = re.match(pattern, str2)
    resobj = re.match(pattern, str3)
    print(resobj)


# 检索字符串中是否包含【正则样式pattern】，只会检索到第一个
def reSearch():
    pattern = "[Pp]ython"
    str1 = "天不生python，世间万古如长夜"
    str2 = "python一出谁与争疯"
    str3 = "天不生python，世间万古如长夜；农不务Python，地头一篇荒草丛；劳资不学拍森，劳资吃什么！"
    resobj = re.search(pattern, str1)
    resobj = re.search(pattern, str2)
    resobj = re.search(pattern, str3)
    print(resobj)


# 从字符串中检索出全部满足【正则样式patten】的子串，形成列表
def reFindall():
    pattern = "[Pp]ython|拍森|派森"
    str1 = "天不生python，世间万古如长夜"
    str2 = "Python一出谁与争疯"
    str3 = "天不生python，世间万古如长夜；农不务Python，地头一篇荒草丛；劳资不学拍森，劳资吃什么！派森真牛逼~"
    reslist = re.findall(pattern, str1)
    reslist = re.findall(pattern, str2)
    reslist = re.findall(pattern, str3)
    print(reslist)


# 将字符串中满足【正则样式pattern】的子串全部替换为指定字符串，并返回替换后的新字符串
def reSub():
    pattern = "[Pp]ython|拍森|派森"
    str1 = "天不生python，世间万古如长夜；农不务Python，地头一片荒草丛；劳资不学拍森，劳资吃什么！派森真牛逼~"
    # 把str1中满足pattern样式的子串全部替换为"【大拍森】"，返回替换后的结果字符串
    resstr = re.sub(pattern, "【大拍森】", str1)
    print(resstr)


if __name__ == "__main__":
    # reMatch()
    # reSearch()
    # reFindall()
    # reSub()

    print("main over")
