#爬取新闻
#首页所有新闻内容
import urllib.request
import re
import urllib.error
'''
1.爬取首页，得到链接
2.有无Frame
3.有，抓取frame对应网页内容；无，直接抓取当前页面
'''
try:
    url = "http://news.qq.com/"
    data = urllib.request.urlopen(url).read().decode("UTF-8","ignore")
    pat = '<a target="_blank" class="linkto" href="(.*?)">'
    #所有链接
    alllink = re.compile(pat).findall(data)
    print(len(alllink))
    #循环爬取所有链接
    for i in range(0,len(alllink)):
        try:
            thislink = alllink[i]
            thispage = urllib.request.urlopen(thislink).read().decode("gb2312","ignore")
            pat2 = "<frame src=(.*?)>"
            isframe = re.compile(pat2).findall(thispage)
            if(len(isframe)==0):
                #直接爬
                print(i)
                urllib.request.urlretrieve(thislink,"f:\\网页\\"+str(i)+".html")
            else:
                #得到frame的网址爬
                flink = isframe[0]
                urllib.request.urlretrieve(flink,"f:\\网页\\"+str(i)+".html")
        except urllib.error.URLError as err:
            if hasattr(err,'code'):
                print(err.code)
            if hasattr(err,'reason'):
                print(err.reason)
except urllib.error.URLError as err:
    if hasattr(err,'code'):
        print(err.code)
    if hasattr(err,'reason'):
        print(err.reason)

        






    
