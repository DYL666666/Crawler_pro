# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class TonghuashPipeline:
    def process_item(self, item, spider):
        return item
class ShfyPipeline:
    def process_item(self, item, spider):
        self.save_csv(item)
    def save_csv(self,item):
        with open('shfy.csv','a+',encoding='utf-8') as f:
            f.write(item['ah'])
            f.write(item['title'])
            f.write(item['wslb'])
            f.write(item['ay'])
            f.write(item['department'])
            f.write(item['level'])
            f.write(item['date'])
            f.write('\n')
class HuazpPipeline:
    def __init__(self):
        self.conn = pymysql.connect(host='localhost', user='root', passwd='dyl@3654', db='mysql', charset='utf8')
        self.cur = self.conn.cursor()
        # self.create_huazp_db()#创表
        self.data = []

    def close_spider(self,spider):
        if len(self.data) > 0:#防止最后电影不足100条
            self._write_to_db()
        self.conn.close()

    def _write_to_db(self):
        sql = '''
                        insert into huazp(qy_name,product_id,product_xm,qy_zs,qy_address,shxy_id,fddb_man,qyfz_man,zlfz_man,fzjg,qf_man,daily_jg,daily_man,yx_time,fz_time,state,complaint_hotline)
                        values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)'''
        self.cur.executemany(sql, self.data)
        self.conn.commit()

    def process_item(self,item,spider):
        # qy_name = item.get('qy_name','')#字典使用:若没有值，则返回默认值‘’
        self.data.append((item['qy_name'], item['product_id'], item['product_xm'], item['qy_zs'], item['qy_address'], item['shxy_id'],
            item['fddb_man'], item['qyfz_man'], item['zlfz_man'], item['fzjg'], item['qf_man'], item['daily_jg'],
            item['daily_man'], item['yx_time'], item['fz_time'], item['state'], item['Complaint_hotline']))
        if len(self.data) == 100:#模拟批处理，100条在进行保存
            self._write_to_db()
            self.data.clear()
        return item

    def create_huazp_db(self):
        sql = '''
            create table huazp(
            qy_name varchar(255),
            product_id varchar(255),
            product_xm varchar(255),
            qy_zs varchar(255),
            qy_address varchar(255),
            shxy_id varchar(255),
            fddb_man varchar(255),
            qyfz_man varchar(255),
            zlfz_man varchar(255),
            fzjg varchar(255),
            qf_man varchar(255),
            daily_jg varchar(255),
            daily_man varchar(255),
            yx_time varchar(255),
            fz_time varchar(255),
            state varchar(255),
            complaint_hotline varchar(255))
            '''
        conn = pymysql.connect(host='localhost', user='root', passwd='dyl@3654', db='mysql', charset='utf8')
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        # cur.close()
        # conn.close()

    def save_huazp_csv(self,item):
        with open('huazp.csv','a+',encoding='utf-8')as f:
            f.write(item['qy_name']+"\t")
            # f.write(item['product_id']+"\t")
            # f.write(item['product_xm']+"\t")
            # f.write(item['qy_zs']+"\t")
            f.write(item['qy_address']+"\t")
            f.write(item['shxy_id']+"\t")
            # f.write(item['fddb_man']+"\t")
            # f.write(item['qyfz_man']+"\t")
            # f.write(item['zlfz_man']+"\t")
            f.write(item['fzjg']+"\t")
            # f.write(item['qf_man']+"\t")
            f.write(item['daily_jg']+"\t")
            # f.write(item['daily_man']+"\t")
            f.write(item['yx_time']+"\t")
            f.write(item['fz_time']+"\t")
            # f.write(item['state']+"\t")
            # f.write(item['Complaint_hotline'])
            f.write('\n')
class  MeituanPipline:
    def process_item(self, item, spider):
        #self.save_meituan_csv(item)
        pass




