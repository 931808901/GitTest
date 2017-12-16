#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import csv
import re
from urllib.request import urlretrieve

import requests


def printList(mlist):
    for item in mlist:
        print(item)

def downloadImg(url,filepath):
    urlretrieve(url,filename=filepath)
    print(filepath,"下载完毕！")

def downloadFile(url,filepath):
    urlretrieve(url,filename=filepath)
    print(filepath,"下载完毕！")

def writeCsvFile(filePath,iterator):
    # 存入CSV
    with open(filePath,"w",newline="") as file:
        csvWriter = csv.writer(file)
        for item in iterator:
            csvWriter.writerow([item])
    print("写入成功！")

def readCsvFile(filePath):
    dataList = []
    with open(filePath, "r") as file:
        reader = csv.reader(file)
        for item in reader:
            dataList.append(item)
    return dataList

def getUrls(url):
    try:
        # 不允许重定向（如果url存在服务器的重定向，就视为一个无效的url）
        html = requests.get(url,allow_redirects=False).text
        return re.findall("<a.+ href=\"(https?://.+?)\"", html)
    except Exception as e:
        print("通信异常")

    return []