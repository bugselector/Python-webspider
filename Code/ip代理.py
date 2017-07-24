#构建代理ip
#import urllib.request
'''
ip = "218.73.143.244"
proxy = urllib.request.ProxyHandler({"http":ip})
opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
urllib.request.install_opener(opener)
url = "http://www.baidu.com"
data = urllib.request.urlopen(url).read().decode('utf-8')
data1 = urllib.request.urlopen(url).read()
print(len(data))
fh = open('f:/ip_baidu.html','wb')
fh.write(data1)
fh.close()
'''
'''
#IP代理池构建的第一种方案(适合代理IP稳定)
import random
import urllib.request
ippools = [
    "122.226.168.180",
    "61.191.41.130",
    "115.231.175.68",
    ]

def ip(ippools):
    thisip = random.choice(ippools)
    print(thisip)
    proxy = urllib.request.ProxyHandler({"http":thisip})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

for i in range(0,3):
    try:
        ip(ippools)
        url = "http://www.baidu.com"
        data1 = urllib.request.urlopen(url).read()
        print(len(data1))
        fh = open('f:/ip_baidu.html','wb')
        fh.write(data1)
        fh.close()
    except Exception as err:
        print(err)
'''

#IP代理池构建的第二种方案(适合代理IP不稳定):接口调用
import urllib.request
import random
import re

def api():
    print("调用了一次接口")
    data = urllib.request.urlopen("http://api.xicidaili.com/free2016.txt").read()
    allip = re.compile("(\d*?\.\d*?\.\d*?\..*?)\r\n").findall(data.decode('utf-8'))
    ippools=[]
    for item in allip:
        ippools.append(item)
    return ippools

def ip(ippools,time):
    thisip = ippools[time]
    print("当前用的IP："+thisip)
    proxy = urllib.request.ProxyHandler({"http":thisip})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

x = 0
for i in range(0,35):
    try:
        if x%10 == 0:
            ippools = api()
            ip(ippools,x%10)
        else:
            ip(ippools,x%10)
        url = "http://www.baidu.com"
        data1 = urllib.request.urlopen(url).read()
        print(len(data1))
        fh = open('f:\\ip接口调用\\'+str(i)+'.html',"wb")
        fh.write(data1)
        fh.close()
        x+=1
    except Exception as err:
        print(err)
        x+=1


