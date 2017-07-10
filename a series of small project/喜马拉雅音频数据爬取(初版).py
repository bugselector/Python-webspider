import urllib.request
from lxml import etree
import random
import re

#爬取喜马拉雅网站的音频数据(http://www.ximalaya.com/dq/all/1/)
#目标：获取每个专辑的 名称、图片链接、专辑里的声音详细链接

#用户代理
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

#获取单页专辑信息
def get_one_page(url):
    allinfo = []
    ua()
    data = urllib.request.urlopen(url).read().decode("utf-8")
    #print(len(data))
    treedata = etree.HTML(data)

    #专辑名称
    pd_name = treedata.xpath('//div[@class="albumfaceOutter"]/a/span/img/@alt')
    #print(pd_name)
    allinfo.append(pd_name)

    #图片链接
    img_url = treedata.xpath('//div[@class="albumfaceOutter"]/a/span/img/@src')
    #对连接进行处理，得到更清晰的图片
    img = []
    for each in img_url:
        img.append(re.sub("_web_large","",each))
    #print(img)
    allinfo.append(img)

    #频道链接
    pd_url = treedata.xpath('//div[@class="albumfaceOutter"]/a/@href')
    #print(pd_url)
    allinfo.append(pd_url)

    return allinfo

#提取专辑内的所有声音的链接all_sound_url
def parse_album(all_pd_url):
    all_sound_url = []
    for each in all_pd_url:
        data = urllib.request.urlopen(each).read().decode("utf-8")
        #print(len(data))
        #正则提取id
        pat = '<li sound_id="(.*?)" class="">'
        rst = re.compile(pat).findall(data)
        #print(rst)
        #专辑内声音链接
        link = re.sub(re.split("/",each)[-1],"",re.sub("album","sound",each))
        all_sound = []
        for k in rst:
            all_sound.append(link+k)
        all_sound_url.append(all_sound)
    '''
    for each in all_sound_url:
        print(len(each))
        print(each)
    '''
    return all_sound_url

def main():
    for i in range(1,6):
        url = "http://www.ximalaya.com/dq/all/"+str(i)+"/"
        page_info = get_one_page(url)
        all_title = page_info[0]
        all_img = page_info[1]
        all_sound_url = parse_album(get_one_page(url)[2])
        for k in range(0,len(all_title)):
            print(all_title[k])
            print(all_img[k])
            print(all_sound_url[k])

if __name__ == "__main__":
    main()