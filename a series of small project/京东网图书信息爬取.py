import urllib.request
import re

count = 0
for k in range(1,5):
	url = "https://list.jd.com/list.html?cat=1713,3258,3307"+"&page="+str(k)
	data = urllib.request.urlopen(url).read().decode("utf-8","ignore")
	#print(len(data))
	pat1 = '<a href="//book.jd.com" class="crumbs-link">(.*?)</a>'
	h1 = re.compile(pat1).findall(data)
	print(h1[0])
	pat2 = '<div class="trigger"><span class="curr">(.*?)</span>'
	h2 = re.compile(pat2).findall(data)
	print(h2[0])
	pat3 = '<h3><b>(.*?)</b><em>'
	h3 = re.compile(pat3).findall(data)
	print(h3[0])
	#当前搜索商品的总页数
	pat4 = '<em>/</em><i>(.*?)</i>'
	pages = re.compile(pat4).findall(data)
	print("总页数:"+pages[0])
	#书名
	pat5 = '<div class="p-name">.*?<em>(.*?)</em>'
	alltitle = re.compile(pat5,re.S).findall(data)
	#print("书名:"+alltitle[-2])
	#作者
	pat6 = '<div class="p-bookdetails">.*?<a title="(.*?)"'
	writer = re.compile(pat6,re.S).findall(data)
	#print("作者:"+writer[-2])
	#出版社
	pat7 = '<span class="p-bi-store">.*?<a title="(.*?)"'
	press = re.compile(pat7,re.S).findall(data)
	#print("出版社:"+press[-2])
	#出版时间
	pat8 = '<span class="p-bi-date">(.*?)</span>'
	ptime = re.compile(pat8,re.S).findall(data)
	#print("出版时间:"+ptime[-2].strip())
	for each in range(1,len(writer)):
		try:
			count +=1
			print("第"+str(count)+"本书")
			print("书名:"+alltitle[each])
			print("作者:"+writer[each])
			print("出版社:"+press[each])
			print("出版时间:"+ptime[each].strip())
			print("\n")
		except Exception as err:
			print(err)

