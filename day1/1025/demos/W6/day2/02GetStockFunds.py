#! C:\Python36\python.exe
# coding:utf-8
'''
·从东方财富网爬取股票型基金走势数据
·http://quote.stockstar.com/fund/stock_3_1_1.html
·将爬到的数据写入CSV文件
'''
import csv
import re
import threading

import requests


# <td class="align_center "><a href="http://fund.stockstar.com/funds/000042.shtml">000042</a></td>
# <td class="align_left">中证财通可持续发展100指数A</td>

# 表格内容的正则
reTbody = "<tbody[\s\S]+</tbody>"#[\s\S]代表所有任意字符，包括空格和换行
# reTbody = re.compile(reTbody,re.DOTALL)#re.DOTALL=声明【.】可以代表任意字符包括换行符
reTbody = re.compile(reTbody)

# reTarget = "<td .+>(<a .+>)?(\w+)(</a>)?</td>"
# reTarget = "<td .+?>(.+?)</td>"
# 标签内文本的正则
reTarget = ">([\w-].+?)<"
reTarget = re.compile(reTarget)

# 爬取一页的信息
def getPageData(url):
    # 得到表格部分的html代码
    html = requests.get(url).text
    # print(html)
    tbody = reTbody.findall(html)[0]  # 经过分析，html中只有一个表格
    # 从tbody中得到所有标签内的文本
    retList = reTarget.findall(tbody)
    # print(len(retList))
    # printList(retList)
    # 每10个元素包装为一条记录
    recordList = []
    for i in range(0, len(retList), 10):
        # print(retList[i])
        rowlist = []
        for j in range(10):
            rowlist.append(retList[i + j])
        print(rowlist)
        recordList.append(rowlist)

    # 逐个记录地写入CSV
    with  open("C:/Users/idea/Desktop/股票型基金走势.csv", "a", newline="") as file:
        csvWriter = csv.writer(file)
        for rowlist in recordList:
            csvWriter.writerow(rowlist)


if __name__ == "__main__":

    # 动态生成全部地址
    urlList = []
    for i in range(1,4):
        url = "http://quote.stockstar.com/fund/stock_3_1_"+str(i)+".html"
        urlList.append(url)

    # 多线程抓取所有页面的基金信息
    tlist = []
    for url in urlList:
        t = threading.Thread(target=getPageData,args=(url,))
        t.start()
        tlist.append(t)

    # 主线程等待工作线程结束
    for t in tlist:
        t.join()

    print("写入成功！")
    print("main over")