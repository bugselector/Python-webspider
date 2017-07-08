# -*- coding: utf-8 -*-
import pymysql

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class DangdangPipeline(object):
    def process_item(self, item, spider):
        conn = pymysql.connect(host="127.0.0.1",user="root",passwd="13518529311",db="dd")
        for i in range(0,len(item["title"])):
            title = item["title"][i]
            link = item["link"][i]
            comment = item["comment"][i]
            #print(title+":"+link+":"+comment)
            sql = "insert into user(name) values('"+rst[each]+"')"
            #print(sql)
            try:
                conn.query(sql)
                conn.commit()
            except Exception as err:
                print(err)
        conn.close()
        return item
