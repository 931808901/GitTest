#! C:\Python36\python.exe
# coding:utf-8
'''
代码统计器
'''

# 统计单个文件的代码量
import os
from tkinter import filedialog


def analyzePyFile(filepath):
    # 预定义结果
    totalLines = 0
    blankLines = 0
    commentLines = 0
    effectiveLines = 0

    # 读入所有行，形成行列表
    file = open(filepath, "r", encoding="utf-8")
    lineList = file.readlines()
    file.close()
    # 统计总行数：列表长度即为总行数
    totalLines = len(lineList)
    # 记录当前是否位于多行注释内部
    betweenComment = False
    for line in lineList:

        # 统计空行数：\n
        if line.strip() == "":
            blankLines += 1

        # 统计自封闭的多行注释
        elif line.strip().startswith("'''") and line.strip().endswith("'''"):
            commentLines += 1

        # 统计多行注释开头
        elif line.strip().startswith("'''") and betweenComment == False:
            betweenComment = True
            commentLines += 1

        # 统计多行注释的结尾
        elif line.strip().endswith("'''") and betweenComment == True:
            commentLines += 1
            betweenComment = False

        # 统计多行注释的身体
        elif betweenComment == True:
            commentLines += 1

        # 统计单行注释
        elif line.strip().startswith("#"):
            commentLines += 1

        # 有效代码
        else:
            effectiveLines += 1

    # 汇总结果
    print("totalLines=", totalLines)
    print("blankLines=", blankLines)
    print("commentLines=", commentLines)
    print("effectiveLines=", effectiveLines)
    canReturn = (blankLines + commentLines + effectiveLines) == totalLines
    print("能回归吗？", canReturn)

    # 如果统计结果不能自圆其说，则将结果清零
    if not canReturn:
        totalLines = 0
        blankLines = 0
        commentLines = 0
        effectiveLines = 0
        print(">" * 10 + dirpath + "统计有误" + "<" * 10)

    return {"totalLines": totalLines, "blankLines": blankLines, "commentLines": commentLines,
            "effectiveLines": effectiveLines}


def analyzeDir(dirpath):

    # 预定义结果
    totalLines = 0
    blankLines = 0
    commentLines = 0
    effectiveLines = 0

    # 获取所有子文件（夹）
    fnameList = os.listdir(dirpath)

    # 遍历子文件（夹）
    for fname in fnameList:
        fname = dirpath + "/" + fname

        # 如果是py文件，就分析之，并兼并分析结果
        if os.path.isfile(fname) and fname.endswith(".py"):
            resDict = analyzePyFile(fname)
            totalLines += resDict["totalLines"]
            blankLines += resDict["blankLines"]
            commentLines += resDict["commentLines"]
            effectiveLines += resDict["effectiveLines"]

        # 如果是其他文件，啥也不干
        elif os.path.isfile(fname) and not fname.endswith(".py"):
            pass

        # 如果是文件夹，就递归分析，并兼并分析结果
        else:
            resDict = analyzeDir(fname)
            totalLines += resDict["totalLines"]
            blankLines += resDict["blankLines"]
            commentLines += resDict["commentLines"]
            effectiveLines += resDict["effectiveLines"]

    # 返回汇总结果
    resDict = {"totalLines": totalLines, "blankLines": blankLines, "commentLines": commentLines,
               "effectiveLines": effectiveLines}
    print("-----{0}文件夹分析结果：{1}----".format(dirpath, resDict))
    return resDict


if __name__ == "__main__":
    # analyzePyFile("./ContactBook.py")

    # 使用文件夹选择对话框定位文件夹
    dirpath = filedialog.askdirectory()

    # 统计
    resDict = analyzeDir(dirpath)

    # 打印结果
    print("=" * 20)
    print("总代码量：%d" % resDict["totalLines"])
    print("总空行数：%d，占比%.2f%%" % (resDict["blankLines"], resDict["blankLines"]*100 / resDict["totalLines"]))
    print("总注释量：%d，占比%.2f%%" % (resDict["commentLines"], resDict["commentLines"]*100 / resDict["totalLines"]))
    print("有效代码：%d，占比%.2f%%" % (resDict["effectiveLines"], resDict["effectiveLines"]*100 / resDict["totalLines"]))

    print("main over")
