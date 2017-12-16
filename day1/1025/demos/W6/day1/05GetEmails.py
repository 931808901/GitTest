#! C:\Python36\python.exe
# coding:utf-8
'''
·爬取任意页面中的所有邮箱，例如：http://tieba.baidu.com/p/2544042204
·将爬到的邮箱数据存储为csv文件
'''
import csv
import re

import requests

from demos.W6.day1.SpiderUtil import printList

url = "http://tieba.baidu.com/p/2544042204"

# fghjkl@ghjkl.ghjk.ghjk
reEmail = "\w+@\w+\.\w+\.?\w*"

if __name__ == "__main__":

    html = requests.get(url).text
    retList = re.findall(reEmail,html,re.ASCII)
    # print(retList)
    printList(retList)

    # 写入CSV
    with open("D:/PyDownload/艺术爱好者邮箱.csv","a",encoding="utf-8",newline="") as file:
        writer = csv.writer(file)
        for email in retList:
            writer.writerow([email])
        file.close()

    print("main over")