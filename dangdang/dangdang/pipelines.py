# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import sqlite3

class DangdangPipeline:
    def process_item(self, item, spider):
        # self.create_db()
        self.save_data(item)

    def save_data(self,item):
        sql='''
        insert into dangd(name,author,score,price,comment_nums,time,p_cbs)values(%s,%s,%s,%s,%s,%s,%s)'''
        conn=sqlite3.connect('dang')
        cur=conn.cursor()
        print(item['name'],item['author'],item['score'],item['price'],item['comment_nums'],item['time'],item['p_cbs'])
        #print(item)
        cur.execute(sql,(item['name'],item['author'],item['score'],item['price'],item['comment_nums'],item['time'],item['p_cbs']))
        conn.commit()
        cur.close()
        conn.close()

    def create_db(self):
        sql='''
        create table dangd(
        name varchar(255),
        author varchar(255),
        score varchar(255),
        price varchar(255),
        comment_nums varchar(255),
        time varchar(255),
        p_cbs varchar(255))
        '''
        conn=sqlite3.connect('dang')
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
        conn.close()

