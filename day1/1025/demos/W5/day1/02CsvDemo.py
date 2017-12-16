#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import csv


def writeCsv():
    datalist = [
        {"name": "张三", "age": 20, "hobby": "看片"},
        {"name": "lisi", "age": 20, "hobby": "coding"},
        {"name": "wangwu", "age": 40, "hobby": "读书"},
        {"name": "zhaoliu", "age": 20, "hobby": "coding"},
    ]
    # 不要设置编码
    fileobj = open("./人员信息.csv","w",newline="")
    csvWriter = csv.writer(fileobj)
    for itemDict in datalist:
        csvWriter.writerow(list(itemDict.values()))
    fileobj.close()
    pass


def readCsv():
    fileobj = open("./人员信息.csv", "r")
    csvReader = csv.reader(fileobj)
    for item in csvReader:
        print(item)


if __name__ == "__main__":
    # writeCsv()
    # readCsv()

    print("main over")