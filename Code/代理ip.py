import urllib.request

try:
	ip = "36.81.84.170"
	proxy = urllib.request.ProxyHandler({"http":ip})
	opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)
	url = "http://www.baidu.com"
	print("正在使用ip:"+str(ip))
	data = urllib.request.urlopen(url).read().decode('utf-8')
	data1 = urllib.request.urlopen(url).read()
	print(len(data))
	fh = open('f:/ip_baidu.html','wb')
	fh.write(data1)
	fh.close()
except Exception as err:
	print("出现异常:"+str(err))