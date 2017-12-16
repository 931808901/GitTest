#! C:\Python36\python.exe
# coding:utf-8
'''
·添加4个数据描点，绘制一条蓝色折线；
·绘制一条直线和一条曲线，使其相交，将结果存储为图片；
·在同一函数中存储两组图表；
·添加标题、坐标说明和图例；
·绘制各国GDP饼状图；
·绘制男女各年龄段人口柱状图；
'''
from matplotlib import pyplot
# 中文支持
pyplot.rcParams['font.sans-serif'] = ['SimHei']
#  用来正常显示中文标签
pyplot.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def helloPyplot():

    # 描点（0,0），（1,1），（2,4）...，使用红色方块作为线型
    pyplot.plot([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 25], "rs")
    pyplot.show()


def helloPyplot2():
    pyplot.plot([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 24], "r--")
    pyplot.plot([0, 1, 2, 3, 4, 5], [0 * 5, 1 * 5, 2 * 5, 3 * 5, 4 * 5, 5 * 5], "b-.")
    pyplot.savefig("./hello.png")
    pyplot.show()

def titleAndLabel():
    ret1 = pyplot.plot([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 24], "r-")
    ret2 = pyplot.plot([0, 1, 2, 3, 4, 5], [0 * 3, 1 * 3, 2 * 3, 3 * 3, 4 * 3, 5 * 3], "b-.")

    # 添加标题
    # pyplot.title("What a fucking day!")
    # pyplot.xlabel("the number")
    # pyplot.ylabel("function value")
    pyplot.title(u"函数走势图")

    # 添加坐标轴标签
    pyplot.xlabel(u"X轴")
    pyplot.ylabel("Y轴")

    # 添加图例，第一个元组：图例，第二个元组：说明文字
    pyplot.legend((ret1[0],ret2[0]),("函数y=x**2","函数y=5x"))


    pyplot.savefig("./hello.png")
    pyplot.show()

def saveFigures():

    # 切换到数据1
    pyplot.figure(1)
    pyplot.plot([0, 1, 2, 3, 4, 5], [0, 1, 4, 9, 16, 24], "r--")
    # 保存数据1
    pyplot.savefig("./fig1.png")

    # 切换到数据2
    pyplot.figure(2)
    pyplot.plot([0, 1, 2, 3, 4, 5], [0 * 5, 1 * 5, 2 * 5, 3 * 5, 4 * 5, 5 * 5], "b-.")
    # 存储数据2
    pyplot.savefig("./fig2.png")

    # 显示图表(先后显示1、2)
    pyplot.show()


def showPieChart():
    # pyplot.pie([1,3,1,4,5,2,5])
    pyplot.pie([1, 3, 1, 4, 5, 2, 5], labels=["一", "生", "一", "世", "我", "爱", "我"], startangle=90, counterclock=False)
    pyplot.show()


if __name__ == "__main__":
    # helloPyplot()
    # helloPyplot2()
    # saveFigures()
    # titleAndLabel()
    # showPieChart()

    #
    ages = [0, 10, 20, 30, 40, 50,60,70,80,90,100]
    agePeopleCount = [2,3,20,30,45,25,15,10,5,5,1]
    # 以年龄为横轴，对应的人口数量为纵轴，宽度为0.9，绘制蓝色柱状图
    ret1 = pyplot.bar(ages, agePeopleCount, width=9, color="b")
    ret2 = pyplot.bar(ages,agePeopleCount,width=9,bottom=agePeopleCount,color="r")

    pyplot.title("男女人口分布图")
    pyplot.xlabel("年龄")
    pyplot.ylabel("人口数量")

    pyplot.legend((ret1[0],ret2[0]),("男","女"))
    pyplot.show()

    print("main over")