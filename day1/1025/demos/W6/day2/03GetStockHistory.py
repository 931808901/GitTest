#! C:\Python36\python.exe
# coding:utf-8
'''
·从网易财经爬取所有沪深个股历史数据
·每只个股存入相应的CSV文件
'''
import re
import threading

from demos.W6.day1.SpiderUtil import downloadFile, readCsvFile, printList

# http://quotes.money.163.com/service/chddata.html?code=1+300123+&end=20171030&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP
urlHead = "http://quotes.money.163.com/service/chddata.html?code="
urlTail = "&end=20171030&fields=TCLOSE;HIGH;LOW;TOPEN;LCLOSE;CHG;PCHG;TURNOVER;VOTURNOVER;VATURNOVER;TCAP;MCAP"


def generateUrl(stockCode):
    return urlHead + ("0" if stockCode.startswith("6") else "1") + stockCode + urlTail

def generateFilePath(filename):
    return "D:/PyDownload/"+filename

reStockCode = "\((\d{6})\)"
reStockName = "(\w+)\("
reStockCode = re.compile(reStockCode)
reStockName = re.compile(reStockName)

sem = threading.Semaphore(10)
def myDownloadFile(url,filePath):
    with sem:
        downloadFile(url,filePath)

if __name__ == "__main__":

    # 从CSV文件中读入所有个股
    dataList = readCsvFile("C:/Users/idea/Desktop/沪深个股列表.csv")
    printList(dataList)

    # 多线程下载每只个股的历史走势
    tlist = []
    for i in range(100):
        stockName = dataList[i][0]
        code = reStockCode.search(stockName).group(1)
        name = reStockName.search(stockName).group(1)
        url = generateUrl(code)
        filePath = generateFilePath(code+"_"+name+".csv")

        # 开辟工作线程下载CSV
        t = threading.Thread(target=myDownloadFile,args=(url,filePath))
        tlist.append(t)
        t.start()

    # 让主线程等待工作线程结束
    for t in tlist:
        t.join()

    print("main over")
