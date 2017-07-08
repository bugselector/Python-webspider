# -*- coding: utf-8 -*-
import scrapy
import re
import urllib.request
from scrapy.http import Request
from jianshu.items import JianshuItem

class NovelSpider(scrapy.Spider):
    name = 'novel'
    allowed_domains = ['jianshu.com']
    #start_urls = ['http://jianshu.com/']
    header = {"User-Agent":"ozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0"}
    allurl = []
    for page in range(0,200):
        thisurl = "http://www.jianshu.com/c/dqfRwQ?order_by=commented_at&page="+str(page)
        allurl.append(thisurl)

    def start_requests(self):
        for k in range(0,len(self.allurl)):
            cu_url = self.allurl[k]
            yield Request(cu_url,headers=self.header,callback=self.parse)

    def parse(self, response):
        data = response.body.decode("utf-8")
        item = JianshuItem()
        alltitle = response.xpath("//a[@class='title']/text()").extract()
        pat = '<a class="title" target="_blank" href="(.*?)">'
        rst = re.compile(pat).findall(data)
        alllink = []
        for link in range(0,len(rst)):
            if rst[link] not in alllink:
                alllink.append(rst[link])
        alltitle1 = []
        for link in range(0, len(alltitle)):
            if alltitle[link] not in alllink:
                alltitle1.append(alltitle[link])
        for i in range(0,len(alllink)):
            try:
                thislink = "http://www.jianshu.com//"+alllink[i]
                print(alltitle1[i]+"\n")
                urllib.request.urlretrieve(thislink,"F:\\Python\\Web Spider\\Crawl Data\\简书短篇小说专栏爬取\\"+re.sub("\|","--",alltitle1[i])+".html")
            except Exception as err:
                print("出现异常:"+str(err))

