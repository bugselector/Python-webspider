import urllib.request
import re

#大学排名爬取
for i in range(0,1):
    try:
        url ='http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
        data = urllib.request.urlopen(url,timeout=4).read().decode('utf-8')
        pat1 = '<div align="left">(.*?)</div>'
        pat2 = "<td>(\d*?\\.\d*? )</td>"
        rst1 = re.compile(pat1).findall(data)
        rst2 = re.compile(pat2).findall(data)
        print('\t\t  '+"软科中国最好大学排名2017\n")
        print("{:^10}\t{:^4}\t{:^28}".format("排名","學校名稱","總分"))
        print('\n')
        for i in range(0,50):
            print("{:^10}\t{:^5}\t{:^15}".format(i+1,rst1[i],rst2[i]))
    except Exception as err:
        print('出现异常:'+str(err))


