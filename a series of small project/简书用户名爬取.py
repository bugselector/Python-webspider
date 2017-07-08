# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 12:06:50 2017

@author: Creator
"""

import urllib.request
from lxml import etree
import random
import pymysql

#用户代理池
def ua():
    uapools = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)",
    ]
    thisua = random.choice(uapools)
    print(thisua)
    headers = ("User-Agent",thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)

#网址构造
#传入参数：页数(每页10篇短篇小说)
def getURL(page):
    allurl = []
    for k in range(0,page):
        thisurl = "http://www.jianshu.com/c/dqfRwQ?order_by=added_at&page="+str(k+1)
        allurl.append(thisurl)
    return allurl

def crawlPage(url):
    data = urllib.request.urlopen(url).read().decode("utf-8")
    #print(len(data))
    treedata = etree.HTML(data)
    #<div class="name">
    #<a class="blue-link" target="_blank" href="/u/c51fadbfff00">在下行之</a>
    rst = treedata.xpath("//div[@class='name']/a/text()")
    print(len(rst))
    conn = pymysql.connect(host="127.0.0.1",user="root",passwd="13518529311",db="jianshu",charset='utf8')
    for each in range(0,len(rst)):
        print(rst[each])
        sql = "insert into user(name) values('"+rst[each]+"')"
        #print(sql)
        try:
            conn.query(sql)
            conn.commit()
        except Exception as err:
            print(err)
    conn.close()
def main():
    allurl = getURL(100)
    for i in range(0,len(allurl)):
        try:
            ua()
            thisurl = allurl[i]
            crawlPage(thisurl)
        except Exception as err:
            print("出现异常:"+str(err))
            
if __name__=="__main__":
    main()