import urllib.request
from lxml import etree

url = "https://www.sogou.com/"
data = urllib.request.urlopen(url).read().decode("utf-8")
#先把字符串转化为HTML对象
treedata = etree.HTML(data)
#使用xpath表达式
rst = treedata.xpath("/html/head/title/text()")
print(rst[0])