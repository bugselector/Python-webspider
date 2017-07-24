import urllib.request
from http import cookiejar

cookie = cookiejar.CookieJar()
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
data = opener.open('http://www.baidu.com')
for item in cookie:
	print("name:"+item.name)
	print("value:"+item.value)