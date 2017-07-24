import urllib.request
import re
import random

uapools = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)",
    ]

def ua(uapools):
    thisua = random.choice(uapools)
    print(thisua)
    headers = ("User-Agent",thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
def crawl(keyname,page):
	key = urllib.request.quote(keyname)
	for i in range(1,page):
		url = "https://s.taobao.com/search?q="+key+"&s="+str((i-1)*44)
		ua(uapools)
		data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
		pat ='"pic_url":"//(.*?)"' 
		imglist = re.compile(pat).findall(data)
		for j in range(0,len(imglist)):
			thisimg = imglist[j]
			thisimgurl = "http://"+thisimg
			localfile = "F:\\Python\\Web Spider\\Crawl Data\\淘宝商品图片爬取\\3\\"+str(i)+str(j)+".jpg"
			urllib.request.urlretrieve(thisimgurl,localfile)

def main():
	crawl("", 22)

if __name__ == '__main__':
	main()
