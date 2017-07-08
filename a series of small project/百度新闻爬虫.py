import urllib.request
import re
import urllib.error

try:
    url = "http://news.baidu.com/"
    data = urllib.request.urlopen(url).read().decode("UTF-8","ignore")
    print(len(data))
    pat = '<a href="(.*?)".*?a>'
    rst = re.compile(pat).findall(data)
    for i in range(0,len(rst)):
        try:
            print(i)
            thislink = rst[i]
            urllib.request.urlretrieve(thislink,"F:\\Python\\Python网络爬虫\\爬取数据\\data\\"+str(i)+'.html')
        except Exception as err:
            print('出现异常'+str(err))
except urllib.error.URLError as err:
    if hasattr(err,'code'):
        print(err.code)
    if hasattr(err,'reason'):
        print(err.reason)
