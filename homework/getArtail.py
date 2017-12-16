# coding:utf-8
import re
import threading
from urllib.request import urlretrieve

import requests
"<li class=\"list_r1\"><a href=\"(http.+?)\".*>"
reUrl = "<li class=\"list_r1\"><a href=\"(http.+?)\".*>"
reUrl = re.compile(reUrl)

reTitle="<title>(.+?)</title>"
reTitle=re.compile(reTitle)

reContent="<p>(.+?)</p>"
reContent=re.compile(reContent)

if __name__ == '__main__':
    html = requests.get("http://www.jj59.com/49/" ).text
    retList = reUrl.findall(html)
    html1 = requests.get(retList[1]).text
    title=reTitle.findall(html1)[0]
    print(title.encode('utf-8'))
    content=reContent.findall(html1)[0]
    print(type(title))
    a='1234'
    print(type(a))
    # print(content.encode('gbk'))
    f=open('1.txt','w')
    f.write(title)
    # f.write(content)
    f.close()