#coding=utf-8
import re
import requests,pymysql

#提取新闻信息
def extractingInformation(url):
    information=[]
    # resp = requests.get('http://news.ycwb.com/2017-07/27/content_25279234.htm')
    resp = requests.get(url)
    mBytes = resp.content
    html = mBytes.decode("utf-8")
    # print(html)
    patterm1 = r'<span id="pubtime_baidu">.*?</span>'
    patterm2 = r'<span id="author_baidu">.*?</span>'
    patterm3 = r'<title>.*?</title>'
    patterm4 = r'<span id="source_baidu">.*?</span>'
    data = re.findall(patterm1, html)
    data = data[0].split('>')[1].split('<')[0]
    information.append(data)
    author=re.findall(patterm2, html)
    author=author[0].split('>')[1].split('<')[0]
    information.append(author)
    title=re.findall(patterm3, html)
    title=title[0].split('>')[1].split('<')[0]
    information.append(title)
    source=re.findall(patterm4, html)
    source=source[0].split('>')[1].split('<')[0]
    information.append(source)
    #返回值：日期，作者，标题，来源
    return information

#将信息写入数据库
def writeInformationTOmysql(information):
    try:
        conn = pymysql.connect(host='localhost', port=3306, user='root', password='123456', database='world',
                               charset='utf8')
        cur = conn.cursor()
        cur.execute(
            'insert into reporter(name,media) values(%s,%s)' % ('"'+information[1]+'"' ,'"'+information[3]+'"'))
        conn.commit()
        cur.execute('select reporterid  from reporter where name=%s' % ('"'+information[1]+'"'))
        reportid=cur.fetchall()[0][0]
        cur.execute('insert into articles(title,data,media,reporterid) values(%s,%s,%s,%d)' % (
         '"'+information[2]+'"' , '"'+information[0]+'"','"'+information[3]+'"' ,reportid))
        conn.commit()
        cur.close()
        conn.close()
    except Exception as e:
        print(e)


def newsInformation(url):
    information = extractingInformation(url)
    # 将信息写入数据库
    writeInformationTOmysql(information)


if __name__=='__main__':
    #提取信息
    # newsInformation('http://news.ycwb.com/2017-10/26/content_25623427.htm')
    # newsInformation('http://news.ycwb.com/2017-07/27/content_25279234.htm')
    # newsInformation('http://sports.ycwb.com/2017-10/29/content_25629641.htm')
    # newsInformation('http://sports.ycwb.com/2017-10/29/content_25629655.htm')
    # newsInformation('http://edu.ycwb.com/2017-09/22/content_25525792.htm')
    # newsInformation('http://edu.ycwb.com/2017-09/18/content_25508307.htm')
    newsInformation('http://culture.ycwb.com/2017-09/16/content_25503619.htm')
    newsInformation('http://culture.ycwb.com/2017-09/13/content_25490942.htm')
    newsInformation('http://culture.ycwb.com/2017-09/12/content_25487937.htm')
    print('main over')