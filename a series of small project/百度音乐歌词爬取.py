# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 08:56:16 2017

@author: Creator
"""

import urllib.request
import random
from lxml import etree

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
    
#热歌榜top500    
def getAllURL(url):
    ua()
    data = urllib.request.urlopen(url).read().decode("utf-8")
    #print(len(data))
    treedata = etree.HTML(data)
    #<span class="song-title " style='width: 240px;'><a href="/song/276867440" target="_blank" title="李玉刚刚好遇见你" data-film="null">刚好遇见你</a></span>
    rst = treedata.xpath("//span[@class='song-title ']/a[@data-film='null']/@href")
    print(len(rst))
    allurl = []
    for each in range(0,len(rst)):
        thisurl = "http://music.baidu.com"+rst[each]
        print(thisurl)
        allurl.append(thisurl)
    return allurl
    
def getLyric(url):
    data = urllib.request.urlopen(url).read().decode("utf-8")
    treedata = etree.HTML(data)
    #<div id="lyricCont" class="lyric-content" style="display: none;" data-lrclink="http://musicdata.baidu.com/data2/lrc/1458419/1458419.lrc"></div>
    rst = treedata.xpath("//div[@id='lyricCont']/@data-lrclink")
    #print(rst)
    #<div id="show69-sidebar"><a target="_blank" class="title log">刚好遇见你</a>
    title = treedata.xpath("//div[@id='show69-sidebar']/a/text()")
    urllib.request.urlretrieve(rst[0],"F:\\Python\\Web Spider\\Crawl Data\\百度音乐歌词\\"+title[0]+".lrc")

def main():
    url = "http://music.baidu.com/top/dayhot"
    allURL = getAllURL(url)
    for i in range(0,len(allURL)):
        try:
            ua()
            getLyric(allURL[i])
        except Exception as err:
            print(err)
main()
        
