#! C:\Python36\python.exe
# coding:utf-8
'''
·从东方财富网爬取沪深个股列表
·http://quote.eastmoney.com/stocklist.html
·将爬到的数据写入CSV文件
'''

# <a target="_blank" href="http://quote.eastmoney.com/sz300638.html">广和通(300638)</a>
import csv
import re

import requests

from demos.W6.day1.SpiderUtil import printList, writeCsvFile

reStock = "<a .+>(\w+\(\d{6}\))</a>"
reStockCode = "\d{6}"

reStock = re.compile(reStock)
reStockCode = re.compile(reStockCode)

if __name__ == "__main__":

    html = requests.get("http://quote.eastmoney.com/stocklist.html").content.decode("gbk")
    # print(html)

    retList = reStock.findall(html)
    # printList(retList)

    # 清洗数据
    # 沪深个股必须是0、3、6开头
    finalList = []
    for stock in retList:
        stockCode = reStockCode.search(stock).group()
        # print(stockCode)

        if stockCode.startswith("0") or stockCode.startswith("3") or stockCode.startswith("6"):
            finalList.append(stock)

    print(len(finalList))
    printList(finalList)

    # 存入CSV
    writeCsvFile("C:/Users/idea/Desktop/沪深个股列表.csv",finalList)

    print("main over")