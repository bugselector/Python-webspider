import urllib.request
import re
import urllib.error
import random

ippools = [
	"42.123.77.119",
	"116.226.90.12",
	"139.224.237.33",
	"58.209.151.126"
	]
uapools = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)",
    ]

def ip_ua(ippools):
	headers = ("User-Agent",random.choice(uapools))
	thisip = random.choice(ippools)
	print("当前使用IP："+str(thisip))
	proxy = urllib.request.ProxyHandler({"http":thisip})
	opener = urllib.request.build_opener(proxy,urllib.request.ProxyHandler)
	opener.addheaders = [headers]
	urllib.request.install_opener(opener)

try:
	for i in range(0,4):
		try:
			ip_ua(ippools)
			url = "http://www.qiushibaike.com/8hr/page/"+str(i)+"/?s=4985364"
			data = urllib.request.urlopen(url).read().decode('utf-8')
			pat = '<div class="content">\s*?<span>(.*?)</span>'
			rst = re.compile(pat).findall(data)
			for j in range(0,len(rst)):
				print(rst[j])
				print("........")
		except urllib.request.HTTPError as err:
			if hasattr(err, 'code'):
				print(err.code)
			if hasattr(err, 'reason'):
				print(err.reason)
except Exception as err:
	print("出现异常:"+str(err))