#异常处理
'''
URLError:
1.连不上服务器
2.远程URL不存在
3.无网络
4.触发HTTPError
'''
'''
import urllib.request
import urllib.error
try:
    urllib.request.urlopen("http://blog.csdn.net/")
except urllib.error.URLError as err:
    if hasattr(err,'code'):
        print(err.code)
    if hasattr(err,'reason'):
        print(err.reason)
'''
#浏览器伪装
import urllib.request
url = "http://blog.csdn.net/"
#格式:元组header=("User_Agent",值)
headers = ("User_Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders=[headers]
data = opener.open(url).read()
fh = open('f:\\1.txt','wb')
fh.write(data)
fh.close()

#1.将opener()安装为全局，让urlopen访问时也添加对应报头
#2.使用Request进行报头添加

























