# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import pymysql
class BookPipeline:
    def process_item(self, item, spider):
        return item
class MySqlPipeLine:
    def process_item(self,item,spider):
        self.conn = pymysql.connect(host='localhost', user="root", passwd="dyl@3654", db="mysql", charset="utf8")
        print("create_db")
        # print(item)
        # self.create_db()
        print("savae_db")
        self.save_db(item)
        return item

    def create_db(self):
        sql='''create table shuqi_db(
        title varchar(50),
        intra varchar,
        tpn varchar(50),
        author varchar(50)
        )'''

        cur=self.conn.cursor()
        cur.execute(sql)
        self.conn.commit()
        cur.close()
        self.conn.close()
    def save_db(self,item):

        sql='''
        insert into shuqi_db(title,intra,tpn,author)values(%s,%s,%s,%s)'''
        cur=self.conn.cursor()
        cur.execute(sql,(item['title'],item["introduction"],item["type"],item["author"]))
        print(item['title'], item["introduction"], item["type"], item["author"])
        self.conn.commit()
        cur.close()
        self.conn.close()
