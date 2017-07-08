import urllib.request
import re
import urllib.error

try:
	url = "http://blog.csdn.net/?&page="
	for k in range(1,3):
		try:
			url = url + str(k)
			headers = ("User_Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
			opener = urllib.request.build_opener()
			opener.addheaders=[headers]
			#安装为全局
			urllib.request.install_opener(opener)
			data = opener.open(url).read().decode("utf-8")
			pat = '<h3  class="tracking-ad" data-mod="popu_254"><a href="(.*?)"  target="_blank">'
			pat1 = '<h3  class="tracking-ad" data-mod="popu_254"><a href=".*?"  target="_blank">(.*?)</a></h3>'
			rst = re.compile(pat).findall(data)
			rst1 = re.compile(pat1).findall(data)
			for i in range(0,len(rst)):
				try:
					print("正在爬取第"+str(i+1)+"篇博客文章"+"\n")
					thislink = rst[i]
					urllib.request.urlretrieve(thislink,"F:\\Python\\Python网络爬虫\\爬取数据\\CSDN博客文章\\"+str(rst1[i])+".html")
				except Exception as err:
					print("出现异常"+str(err))
		except Exception as err:
			print("出现异常"+str(err))
except urllib.error.URLError as err:
	if hasattr(err,'code'):
		print(err.code)
	if hasattr(err,'reason'):
		print(err.reason)
