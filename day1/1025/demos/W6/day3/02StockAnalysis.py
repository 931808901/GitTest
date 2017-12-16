#! C:\Python36\python.exe
# coding:utf-8
'''
·统计招商银行2017年股价的平均数；
·统计招行2017年股价的中位数；
·求招行2017年股价的方差和标准差；
'''
import csv

# filePath = "‪C:\\Users\\idea\\Desktop\\600036.csv"
# filePath = r"‪C\Users\idea\Desktop\600036.csv"
filePath = "D:/downloads/600036.csv"

if __name__ == "__main__":
    file = open(filePath, "r")
    csvReader = csv.reader(file)

    totalPrice = 0
    dayCount = 0
    priceList = []

    for item in csvReader:
        # print(item)

        # 只读2017年的数据
        if item[0].startswith("2017"):
            # print(item)
            dayPrice = eval(item[3])
            priceList.append(dayPrice)

            totalPrice += dayPrice
            dayCount += 1

    avgPrice = totalPrice / dayCount
    print("2017年的平均股价是%.2f" % (avgPrice))

    priceList.sort()
    print(priceList)
    print("2017年股价中位数是%.2f" % (priceList[dayCount // 2] if len(priceList) % 2 == 1 else (priceList[dayCount // 2] +
                                                                                         priceList[
                                                                                             dayCount // 2 - 1]) / 2))

    # 计算股价方差、标准差
    total = 0
    for price in priceList:
        total += (price - avgPrice) ** 2
    variance = total / len(priceList)
    print("2017年股价方差是%.2f" % (variance))
    print("2017年股价标准差是%.2f元" % (variance**(0.5)))

    file.close()
    print("main over")
