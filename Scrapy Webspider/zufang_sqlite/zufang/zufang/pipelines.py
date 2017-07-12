# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sqlite3

class ZufangPipeline(object):
    #开启爬虫：连接SQLite
    def open_spider(self,spider):
        self.con = sqlite3.connect("zufang.sqlite")
        self.cu = self.con.cursor()
    #数据处理：插入数据
    def process_item(self, item, spider):
        print(spider.name,"piplines")
        insert_sql = "insert into zufang(title,price) " \
                     "values('{}','{}')".format(item["title"],
                                                item["price"])
        print(insert_sql)
        self.cu.execute(insert_sql)
        self.con.commit()
        return item
    #关闭爬虫：关闭数据库连接
    def spider_close(self,spider):
        self.con.close()
