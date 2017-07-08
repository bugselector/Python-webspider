import urllib.request
import re


def pretends():
	headers = ("Uesr-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
	opener = urllib.request.build_opener()
	opener.addheaders = [headers]	
	urllib.request.install_opener(opener)

def crawl(keyword,page):
	key = urllib.request.quote(keyword)
	allurl = []
	for i in range(0,page):
		url = "https://image.baidu.com/search/acjson?tn=resultjson_com&ipn=rj&queryWord="+key+"&word="+key+"&pn="+str(i*30)
		allurl.append(url)
	allurl = list(set(allurl))
	rsturl=[]
	for  k in range(0,len(allurl)):
		try:
			data = urllib.request.urlopen(allurl[k]).read().decode("utf-8")
			#print(len(data))
			pat = ',{"ObjURL":"(.*?)",'
			rst = re.compile(pat).findall(data)
			for j in range(0,len(rst)):
				thisurl = re.sub("\\\/", "/", rst[j])
				if urllib.request.urlopen(thisurl).getcode()==200:
					rsturl.append(thisurl)
					#print(len(rst))
					#print(thisurl)
		except Exception as err:
			print("出现异常:"+str(err))
	return rsturl

def download(imgurl):
	for each in range(0,len(imgurl)):
		try:
			localpath = "F:\\Python\\Web Spider\\Crawl Data\\百度图片\\瀑布流\\"+str(each+1)+".jpg"
			urllib.request.urlretrieve(imgurl[each],localpath)
			print("第"+str(each+1)+"张图片下载成功")
		except Exception as err:
			print(err)
			print("第"+str(each+1)+"张图片下载失败")

def main():
	pretends()
	imgurl = crawl("壁纸",5)
	download(imgurl)

if __name__ == '__main__':
	main()