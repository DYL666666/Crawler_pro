# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
import json

from itemadapter import ItemAdapter

import pymysql
from  twisted.enterprise import adbapi
class FirstspiderPipeline:
    def process_item(self, item, spider):
        print("*"*10)
        # with open("E:\\itcast.json",'a',encoding="utf-8")as f:
        #     item_json=json.dumps(dict(item),ensure_ascii=False,indent=2)
        #     f.write(item_json)
        #     f.write('\n')
        #     print("sccusseful")

        return item
class MySQLPipeline1(object):#同步存储
    def __init__(self):
        self.connect=pymysql.connect(host="localhost",user="root",passwd="dyl@3654",db="mysql")
        self.cursor=self.connect.cursor()
        print("数据库连接成功!")
        self.create_spider()

    def process_item(self,item,spider):

        print("开始往itcast2写入数据")
        insert_sql='''insert into itcast2(teacher,category,experience1,experience2) values (%s,%s,%s,%s)'''
        print(item["teacher"],item["category"],item["experience1"],item["experience2"])
        self.cursor.execute(insert_sql,(item["teacher"],item["category"],item["experience1"],item["experience2"]))
        print("数据写入成功！")
        self.connect.commit()
    def create_spider(self):
        print("创表：")
        create_sql = '''
                        create table itcast2(
                        teacher varchar(50),
                        category varchar(50),
                        experience1 varchar(50),
                        experience2 varchar(50))
                        '''
        self.cursor.execute(create_sql)
        self.connect.commit()
        print("创表成功")
    def close_spider(self,spider):
        print("数据库开始关闭!")
        self.cursor.close()
        self.connect.close()
        print("数据库关闭成功!")


class MySQLPipeline2(object):
    def __init__(self, dbpool):
        self.dbpool = dbpool

    @classmethod
    def from_settings(cls, settings):  # 函数名固定，会被scrapy调用，直接可用settings的值
        """
        数据库建立连接
        :param settings: 配置参数
        :return: 实例化参数
        """
        adbparams = dict(
            host=settings['MYSQL_HOST'],
            db=settings['MYSQL_DBNAME'],
            user=settings['MYSQL_USER'],
            password=settings['MYSQL_PASSWORD'],
            cursorclass=pymysql.cursors.DictCursor  # 指定cursor类型
        )

        # 连接数据池ConnectionPool，使用pymysql或者Mysqldb连接
        dbpool = adbapi.ConnectionPool('pymysql', **adbparams)
        # 返回实例化参数
        return cls(dbpool)

    def process_item(self, item, spider):
        """
        使用twisted将MySQL插入变成异步执行。通过连接池执行具体的sql操作，返回一个对象
        """
        query = self.dbpool.runInteraction(self.do_insert, item)  # 指定操作方法和操作数据
        # 添加异常处理
        query.addCallback(self.handle_error)  # 处理异常

    def do_insert(self, cursor, item):
        # 对数据库进行插入操作，并不需要commit，twisted会自动commit
        insert_sql = """
        insert into lvyou(name1, address, grade, score, price) VALUES (%s,%s,%s,%s,%s)
        """
        self.cursor.execute(insert_sql, (item['Name'], item['Address'], item['Grade'], item['Score'],
                                         item['Price']))

    def handle_error(self, failure):
        if failure:
            # 打印错误信息
            print(failure)









