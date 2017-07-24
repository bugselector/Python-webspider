import urllib.request
'''
#urlretrieve(url,filename)直接下载网页到本地
#urllib.request.urlretrieve("http://www.baidu.com","F:\\dld.html")
#urlcleanup()清除缓存
urllib.request.urlcleanup()
#info()看相应的信息
file=urllib.request.urlopen("http://www.baidu.com")
print(file.info())
#getcode()状态码
print(file.getcode())
#geturl()获取当前爬取页面的url
print(file.geturl())
'''
#超时设置
for i in range(0,100):
    try:
        data = urllib.request.urlopen("http://www.baidu.com",timeout=1)
        print(len(data.read().decode('utf-8')))
    except Exception as err:
        print("出现异常"+str(err))
