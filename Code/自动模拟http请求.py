#get请求
#实现百度搜索信息自动搜索
'''
import urllib.request
import re

key = 'python'
key = urllib.request.quote(key)#如果key为中文，将之用quote()转化
#page = (num-1)*10
for i in range(1,11):
    url = "http://www.baidu.com/s?wd="+key+'&pn='+str((i-1)*10)
    rst = urllib.request.urlopen(url).read().decode('utf-8')
    pat = "title:'(.*?)',"
    pat1 = '"title":"(.*?)",'
    rest = re.compile(pat).findall(rst)
    rest1 = re.compile(pat1).findall(rst)
    for j in range(0,len(rest)):
        print(rest[j])
    for z in range(0,len(rest1)):
        print(rest1[j])
'''

#post请求
import urllib.request
import urllib.parse

posturl = "http://www.baidu.com"
postdata = urllib.parse.urlencode({
    "name":"ceo@163.com",
    "pass":"6666666666"
    }).encode('utf-8')
req = urllib.request.Request(posturl,postdata)
rst = urllib.request.urlopen(req).read().decode('utf-8')
print(len(rst))








