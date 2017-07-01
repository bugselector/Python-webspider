import urllib.request
import re
import random
import pymysql

#IP代理池：其中的代理IP请给据实际情况修改。
def ip():
    ippools = [
    "122.226.168.180",
    "61.191.41.130",
    "115.231.175.68",
    ]
    thisip = random.choice(ippools)
    print(thisip)
    proxy = urllib.request.ProxyHandler({"http":thisip})
    opener = urllib.request.build_opener(proxy,urllib.request.HTTPHandler)
    urllib.request.install_opener(opener)

#用户代理：其中的User-Agent尽量越多越好(但都必须是可用的)
def ua():
    uapools = [
    "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; Maxthon/3.0)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ;  QIHU 360EE)",
    ]
    thisua = random.choice(uapools)
    #print(thisua)
    headers = ("User-Agent",thisua)
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    urllib.request.install_opener(opener)


allcomment = []
conn = pymysql.connect(host="127.0.0.1",user="root",passwd="13518529311",db="tengxunvideo",charset='utf8')

def getComment(starturl):
    data = urllib.request.urlopen(starturl).read().decode("utf-8")
    #提取评论内容
    pat1 = '"content":"(.*?)",'
    #提取评论ID号
    pat2 = '{"id":"(.*?)",'
    comment = re.compile(pat1).findall(data)
    commentid = re.compile(pat2).findall(data)
    for each in comment:
        #对评论内容转码后输出
        #print(eval('u"'+each+'"'))
        allcomment.append(eval('u"'+each+'"'))
        sql = "insert into comment(comment) values('"+eval('u"'+each+'"')+"')"
        try:
            conn.query(sql)
            conn.commit()
        except Exception as err:
            print("写入数据库失败！")
    #使用循环爬取所有页面
    while(len(commentid) > 0):
        for k in range(0,len(commentid)):
            try:
                #使用ip代理
                ip()
                #使用用户代理
                ua()
                url = "https://coral.qq.com/article/1966037100/comment?commentid="+commentid[k]+"&reqnum=50&callback=jQuery"
                #提取评论内容
                pat1 = '"content":"(.*?)",'
                #提取评论ID号
                pat2 = '{"id":"(.*?)",'
                comment = re.compile(pat1).findall(data)
                for each in comment:
                    #对评论内容转码后输出
                    #print(eval('u"'+each+'"'))
                    #把评论内容放入allcomment中
                    allcomment.append(eval('u"'+each+'"'))
                    sql = "insert into comment(comment) values('"+eval('u"'+each+'"')+"')"
                    try:
                        conn.query(sql)
                        conn.commit()
                    except Exception as err:
                        print("写入数据库失败！")
                #如果还要继续爬取更多，使用循环（不过数据量很大，注意伪装和电脑性能）
                commentid = re.compile(pat2).findall(data)
            except Exception as err:
                print(err)

starturl = "https://coral.qq.com/article/1966037100/comment?commentid=0&reqnum=50&callback=jQuery"
getComment(starturl)
conn.close()
print("已爬取总条数:"+str(len(allcomment)))