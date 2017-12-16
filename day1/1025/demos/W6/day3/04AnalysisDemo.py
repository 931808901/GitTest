#! C:\Python36\python.exe
# coding:utf-8
'''
·绘制中国各省地级市数量柱状图、饼状图
'''
import pymysql
from matplotlib import pyplot as pt

# 中文支持
pt.rcParams['font.sans-serif'] = ['SimHei']
pt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

if __name__ == "__main__":
    # 连接数据库获取数据
    conn = pymysql.connect(host="localhost", port=3306, user="root", password="123456", db="world")
    cursor = conn.cursor()
    cursor.execute('''
      select District,count(Name),sum(Population) as p
      from city
      where CountryCode='CHN'
      group by District
      order by p DESC
    ''')
    ret = cursor.fetchall()

    cursor.close()
    conn.close()
    print(ret)

    # 处理数据
    nameList = []
    cityCountList = []
    populationList = []
    labelList = []
    for i in range(len(ret)):
        item = ret[i]
        nameList.append(item[0])
        cityCountList.append(item[1] * 100000 * 3)
        populationList.append(item[2])
        labelList.append(item[0] + ":" + str(item[1]))

    # 绘制饼状图
    # pt.figure(1)
    # pt.pie(cityCountList, labels=labelList, counterclock=False)
    # pt.title("中国各省地级市数量-人口分布图")
    # pt.savefig("./中国各省地级市数量-人口分布图1.png")
    # pt.show()

    # 绘制柱状图
    pt.figure(2)
    rangeList = [x for x in range(len(cityCountList))]
    cityBars = pt.bar(rangeList, cityCountList)
    popuBars = pt.bar(rangeList, populationList, bottom=cityCountList)
    pt.title("中国各省地级市数量-人口分布图")
    pt.xlabel("省份")
    pt.ylabel("地级市数量/人口数量")
    pt.legend((cityBars[0], popuBars[0]), ("地级市数量", "人口规模"))

    for r,c,p,n in zip(rangeList,cityCountList,populationList,nameList):
        # print(r,c,p,n)
        # pt.text(r,c+p+100000*2,n,ha="center",fontsize = 8,fontstyle='italic')
        pt.text(r,c+p+100000*2,n,family='华文行楷',style='italic',verticalalignment='center',horizontalalignment="center", fontsize=10, rotation = 45)

    pt.savefig("./中国各省地级市数量-人口分布图2.png")
    pt.show()

    print("main over")
