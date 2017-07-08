import urllib.request
import urllib.parse
import random

uapools = ["Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0","Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)","Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)",]
def ua(uapools):
    thisua = random.choice(uapools)
    headers = ("User-Agent",thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)
try:
	ua(uapools)
	posturl = "http://192.168.3.5/include/auth_action.php"
	postdata = urllib.parse.urlencode({
		"action":"login",
		"username":"*",
		"password":"*",
		"ac_id":1,
		"user_ip":"",
		"nas_ip":"",
		"user_mac":"",
		"save_me":0,
		"ajax":1,
	    }).encode('utf-8')
	req = urllib.request.Request(posturl,postdata)
	rst = urllib.request.urlopen(req).read().decode("utf-8","ignore")
	print(rst)
	jump_url = "http://192.168.3.5/srun_portal_pc_succeed.php"
	urllib.request.urlretrieve(jump_url,"F:\\Python\\Web Spider\\Crawl Data\\校园网登陆\\登录成功.html")
except Exception as err:
	print(err)