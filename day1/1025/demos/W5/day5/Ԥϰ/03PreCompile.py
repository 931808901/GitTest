#! C:\Python36\python.exe
'''
正则表达式的预编译
对于高频正则表达式，先对其进行预编译，可以大大提高执行速度
'''
import re


def func():
    pass


# 对高频表达式使用预编译机制
def usePreCompile():
    restr = "[Pp]ython|拍森|派森"
    str1 = "Python一出谁与争疯"
    str2 = "天不生python，世间万古如长夜"
    str3 = "天不生python，世间万古如长夜；农不务Python，地头一篇荒草丛；劳资不学拍森，劳资吃什么！派森真牛逼~"
    # 将高频表达式预编译为机器能识别的格式，以便复用时提高执行速度
    pattern = re.compile(restr)
    # 匹配、检索、替换的API都与re的原生API相似
    resobj = pattern.match(str1)
    resobj = pattern.search(str2)
    resobj = pattern.findall(str3)
    resobj = pattern.sub("【大牌森】", str3)
    resobj = pattern.sub("【大牌森】", str3, count=2)
    print(resobj)


if __name__ == "__main__":
    usePreCompile()

    print("main over")
