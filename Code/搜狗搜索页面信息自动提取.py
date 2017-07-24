import urllib.request
import re

try:
    kwd = '最好大学'
    kwd = urllib.request.quote(kwd)
    url = "https://www.sogou.com/sogou?query="+kwd
    data = urllib.request.urlopen(url,timeout=1).read().decode('utf-8')
    print(len(data))
    pat = "<title>(.*?)</title>"
    rst = re.compile(pat).findall(data)
    print(rst)
except Exception as err:
    print(err)
