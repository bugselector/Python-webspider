# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 22:40:31 2017

@author: Creator
"""

import urllib.request
import re
from lxml import etree
import random

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

def getAllURL():
    url = "http://www.kugou.com/yy/rank/home/1-8888.html?from=homepage"
    data = urllib.request.urlopen(url).read().decode("utf-8")
    pat = '<a href="(.*?)".*?class="pc_temp_songname".*?>'
    rst = re.compile(pat).findall(data)
    print(len(rst))
    return rst

def getLyric(url):
    data = urllib.request.urlopen(url).read().decode("utf-8")
    # <div class="displayNone"> 
    treedata = etree.HTML(data)
    rst = treedata.xpath("//div[@class='displayNone']/text()")
    lyric = re.compile(u"[\u4e00-\u9fa5]+").findall(rst[0])
    #print(lyric)
    for each in range(0,len(lyric)):
        print(lyric[each],end=" ")
    print("\n\n")
    
def main():
    ua()
    allurl = getAllURL()
    for each in range(0,len(allurl)):
        try:
            ua()
            getLyric(allurl[each])
        except Exception as err:
            print(err)
            
if __name__ == "__main__":
    main()