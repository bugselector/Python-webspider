import scrapy

#创建一个爬虫类，必须继承scrapy的Spider类
class GanjiSpider(scrapy.Spider):
    #爬虫名称
    name = "zufang"
    #爬取初始url
    start_urls = ["http://zunyi.ganji.com/fang1/"]

    #页面解析函数
    def parse(self, response):
        print(response)
        #标题列表
        title_list = response.xpath('//dd[@class="dd-item title"]/a/text()').extract()
        #价格列表
        price_list = response.xpath('//div[@class="price"]/span[@class="num"]/text()').extract()
        for i,j in zip(title_list,price_list):
            print(i,":",j,"元/月")
