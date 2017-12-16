#! C:\Python36\python.exe
# coding:utf-8
'''
XML解析：
@DOM解析：
·先拿到整颗文档树
·由根元素（文档元素）逐级向叶子节点访问
·逐级访问标签-属性-文本节点
·逻辑通俗，稳定性好（xml如果有语法错误则无法读入整棵树），效率低
----------
@SAX解析：
·从前往后遍历文档流
·遇见标签开始就回调，遇见文本节点就回调，遇见标签闭合就回调
·编码的核心是处理各种情形下的回调
·逻辑灵活，效率高
·缺点是如果xml有语法错误，解析过程会将错就错
'''
import xml.sax
from xml.dom.minidom import parse
from xml.sax import ContentHandler

# dom解析XML
def domParseXml():
    # 解析文件获得文档对象
    dom = parse("../res/1.xml")
    print(type(dom))
    # 获得文档元素
    domTree = dom.documentElement
    mList = []
    # 获得所有标签为movie的元素
    movies = domTree.getElementsByTagName("movie")
    print(type(movies), len(movies))
    # 遍历每一个Movie元素
    for movie in movies:

        # 为每个Movie元素创建字典
        mDict = {}
        print(type(movie))

        # 获得Movie元素的title属性
        title = movie.getAttribute("title")
        mDict["title"] = title

        # 获得标签名叫type的元素们,中的第一个元素,的所有节点中的第一个，的值
        mtype = movie.getElementsByTagName("type")[0].childNodes[0].data
        mDict["type"] = mtype

        format = movie.getElementsByTagName("format")[0].childNodes[0].data
        mDict["format"] = format

        if len(movie.getElementsByTagName("year")) > 0:
            year = movie.getElementsByTagName("year")[0].childNodes[0].data
            mDict["year"] = year

        if len(movie.getElementsByTagName("episodes")) > 0:
            episodes = movie.getElementsByTagName("episodes")[0].childNodes[0].data
            mDict["episodes"] = episodes

        rating = movie.getElementsByTagName("rating")[0].childNodes[0].data
        mDict["rating"] = rating

        stars = movie.getElementsByTagName("stars")[0].childNodes[0].data
        mDict["stars"] = stars

        description = movie.getElementsByTagName("description")[0].childNodes[0].data
        mDict["description"] = description

        mList.append(mDict)
    for item in mList:
        print(item)


# 自定义XML内容处理器
class MyHandler(ContentHandler):

    # 元素开始时回调
    # name=标签名称，attrs=元素的标签内属性
    def startElement(self, tagName, attrs):
        super().startElement(tagName, attrs)
        # print("startElement:",tagName,attrs,type(attrs))

        # 遇见collection元素就创建空列表
        if tagName == "collection":
            self.movieList = []

        # 遇见Movie元素就创建空字典
        elif tagName == "movie":
            self.movieDict = {}
            self.movieDict["title"] = attrs["title"]

    # 遇见文本节点时回调
    # content = 文本
    def characters(self, content):
        super().characters(content)
        # print("characters:", content)

        # 遇见普通文本就记录其值
        if len(content.strip())>0:
            print(content)
            self.currentChars = content

    # 元素闭合时回调
    # name = 标签名称
    def endElement(self, tagName):
        super().endElement(tagName)
        # print("endElement:", name)

        # movie一闭合就将当前字典丢入列表
        if tagName == "movie":
            self.movieList.append(self.movieDict)

        # collection一闭合就打印结果
        elif tagName == "collection":
            # print(self.movieList)
            for movie in self.movieList:
                print(movie)

        # 普通元素一闭合，立即以当前元素名为键，当前文本为值，将键值对存入字典
        else:
            self.movieDict[tagName] = self.currentChars

# sax解析XML
def saxParseXml():
    # 创建sax解析器对象并设置命名空间
    parser = xml.sax.make_parser()
    print(type(parser))  # xml.sax.expatreader.ExpatParser
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    # 为解析器配置内容处理器ContentHandler子类
    # 覆写ContentHandler的相关业务方法
    parser.setContentHandler(MyHandler())
    # 解析文件
    parser.parse("../res/1.xml")


if __name__ == "__main__":

    # domParseXml()
    saxParseXml()

    print("main over")
