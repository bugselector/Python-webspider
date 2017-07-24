#1.腾讯视频评论爬虫(单页评论爬虫)
import urllib.request
import re

#https://video.coral.qq.com/filmreviewr/c/upcomment/[视频ID]e?commentid=[评论ID]&reqnum=[每次提取的评论的个数]

vid = "j6cgzhtkuonf6te"
cid = "6233603654052033588"
num ="20"
url = "https://video.coral.qq.com/filmreviewr/c/upcomment/"+vid+"?commentid="+cid+"&reqnum="+num
headers = {"User_Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
"Content-Type":"application/javascript",
}
opener = urllib.request.build_opener()
headall = []
for key,value in headers.items():
	item = (key,value)
	headall.append(item)
opener.addheaders = headall
urllib.request.install_opener(opener)
#爬取当前评论页面
data = urllib.request.urlopen(url).read().decode('utf-8')
titlepat = '"title":"(.*?)"'
commentpat = '"content":"(.*?)"'
titleall = re.compile(titlepat,re.S).findall(data)
commentall = re.compile(commentpat).findall(data)
print(len(titleall))
for i in range(0,10):
	try:
		title = eval('u"'+titleall[i]+'"')
		content = eval('u"'+commentall[i]+'"')
		sp = "-------------"
		print("评论标题是:"+eval('u"'+titleall[i]+'"'))
		print("评论内容是:"+eval('u"'+commentall[i]+'"'))
		print("-------------")
		with open("F:\\Python\\Web Spider\\Crawl Data\\腾讯视频评论爬取\\comment.txt","a") as f:
			f.write(str(title)+"\n"+str(content)+"\n"+sp)
	except Exception as err:
		print(err)

