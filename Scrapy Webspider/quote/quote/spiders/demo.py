# -*- coding: utf-8 -*-
import scrapy
import re

class DemoSpider(scrapy.Spider):
    name = "demo"
	#这行没有什么用，注释掉
    #allowed_domains = ["toscrape.com"]
	#与爬取链接不同，修改
    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        #此方法返回一个response对象，它就是爬取网页之后返回的东西
	#body属性，直接获取内容
	#正则简单提取一下(先导入re)
        data = response.body.decode("utf-8")
        pat = '<span class="text" itemprop="text">(.*?)</span>'
        rst = re.compile(pat,re.S).findall(data)
        for each in range(0,10):
            print("第"+str(each)+"条:"+rst[each])
        
