import urllib.request
from lxml import etree
import json

def get_one_page(url):
    try:
        response = urllib.request.urlopen(url)
        if response.getcode() == 200:
            return response.read().decode("utf-8")
        else:
            return  None
    except Exception as err:
        return None

def parse_one_page(html):
    treedata = etree.HTML(html)
    #排名
    top = treedata.xpath("//dd/i/text()")
    #图片链接
    img_link = treedata.xpath("//dd/a/img/@data-src")
    #电影名
    mname = treedata.xpath("//div[@class='movie-item-info']/p[@class='name']/a/text()")
    #主演
    mstar = treedata.xpath("//div[@class='movie-item-info']/p[@class='star']/text()")
    #上映时间
    ptime = treedata.xpath("//div[@class='movie-item-info']/p[@class='releasetime']/text()")
    #评分
    score = treedata.xpath("//div[@class='movie-item-number score-num']/p[@class='score']//i/text()")
    rst = []
    for i in range(0, len(score), 2):
        rst.append(score[i] + score[i + 1])
    for i in range(0,len(top)):
        yield {
            'index':top[i],
            'image':img_link[i].rstrip("@160w_220h_1e_1c"),
            'title':mname[i],
            'actor':mstar[i].strip()[3:],
            'time':ptime[i].strip()[5:],
            'score':rst[i]
        }

def write_to_file(content):
    with open("result.txt","a",encoding="utf-8") as f:
        f.write(json.dumps(content,ensure_ascii=False)+"\n")

def main():
    for i in range(0,10):
        url = "http://maoyan.com/board/4?offset="+str(i*10)
        html = get_one_page(url)
        for item in parse_one_page(html):
            print(item)
            write_to_file(item)

if __name__ == "__main__":
    main()