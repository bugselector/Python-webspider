#糗事百科
import urllib.request
import re

headers = ("User-Agent","Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0")
opener = urllib.request.build_opener()
opener.addheaders = [headers]
urllib.request.install_opener(opener)
for k in range(0,10):
	try:
	    url = "http://www.qiushibaike.com/8hr/page/"
	    url = url + str(k) + "/?s=4985076"
	    data = opener.open(url).read().decode('utf-8','ignore')
	    pat = '<div class="content">\s*?<span>(.*?)</span>.*?</div>'
	    rst = re.compile(pat,re.S).findall(data)
	    for i in range(0,len(rst)):
	        print(rst[i])
	        print("----------------")
	except Exception as err:
		print(err)









