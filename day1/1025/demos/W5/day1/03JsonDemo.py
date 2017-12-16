#! C:\Python36\python.exe
# coding:utf-8
'''
about what
'''
import json


# 将（服务端传递过来的）json字符串转换为python字典对象
def readJson():
    jsonStr = '{"name": "张三", "age": 20, "hobby": "看片"}'
    jsonStr = '[{"name":"张三","age":20,"hobby":"看片"},{"name":"李四","age":20,"hobby":"看片"}]'
    pyobj = json.loads(jsonStr,encoding="utf-8")
    print(type(pyobj), pyobj)


# 将字典对象转换为json字符串（用于网络通信）
def writeJson():
    dataDict = {"name": "张三", "age": 20, "hobby": "看片"}
    dataList = [{"name":"张三","age":20,"hobby":"看片"},{"name":"张三","age":20,"hobby":"看片"}]
    outObj = json.dumps(dataDict, ensure_ascii=False)
    outObj = json.dumps(dataList,ensure_ascii=False)
    print(type(outObj), outObj)


if __name__ == "__main__":
    readJson()
    writeJson()
    print("main over")
