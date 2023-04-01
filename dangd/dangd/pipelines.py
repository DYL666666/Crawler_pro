# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class DangdPipeline:
    def process_item(self, item, spider):
        # self.create_dangd_db()
        self.save_dangd_db(item)
    def save_dangd_db(self,item):
        print("正在保存！")
        sql='''
        insert into dangd(named,price,or_price,author,cb_time,cbs,comm_num,dp)values(%s,%s,%s,%s,%s,%s,%s,%s)'''
        conn = pymysql.connect(host='localhost', user='root', passwd='dyl@3654', db='mysql', charset='utf8')
        cur = conn.cursor()
        cur.execute(sql,(item['name'],item['price'],item['or_price'],item['author'],item['cb_time'],item['cbs'],item['comm_num'],item['dp']))
        conn.commit()
        print("保存成功！")
        cur.close()
        conn.close()
    def create_dangd_db():
        sql='''
        create table dangd(
        named varchar(255),
        price varchar(255),
        or_price varchar(255),
        author varchar(255),
        cb_time varchar(255),
        cbs varchar(255),
        comm_num varchar(255),
        dp varchar(255))'''
        conn=pymysql.connect(host='localhost',user='root',passwd='dyl@3654',db='mysql',charset='utf8')
        cur=conn.cursor()
        cur.execute(sql)
        conn.commit()
        print("创表成功！")
        cur.close()
        conn.close()

