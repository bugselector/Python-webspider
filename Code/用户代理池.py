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

for k in range(0,30):
    try:
        ua(uapools)
        url = "http://www.qiushibaike.com/8hr/page/"
        url = url + str(k) + "/?s=4985076"
        data = urllib.request.urlopen(url).read().decode('utf-8','ignore')
        pat = '<div class="content">\s*?<span>(.*?)</span>.*?</div>'
        rst = re.compile(pat,re.S).findall(data)
        for i in range(0,len(rst)):
            print(rst[i])
            print("----------------")
    except urllib.error.URLError as err:
        if hasattr(err,'code'):
            print(err.code)
        if hasattr(err,'reason'):
            print(err.reason)
