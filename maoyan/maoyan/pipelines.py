# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import csv
import os.path

# 爬取字段  电影名，主演，上映时间，评分，电影类型，时长，上映地点，累计票房
class MaoyanPipeline:
    def __init__(self):
        # 打开文件，指定方式为写，利用第3个参数把csv写数据时产生的空行消除
        self.f = open("maoyan.csv","a+",newline="",encoding="utf-8")
        # 设置文件第一行的字段名，注意要跟spider传过来的字典key名称相同
        # self.filenames = ["电影名","主演","上映时间","评分","电影类型","时长","上映地点","累计票房"]
        self.filenames = ['user_id','movie_id','movie_name','actors','release_time','score',
                          'movie_type','duration','release_place','cumulative_box_office']
        # 指定文件的写入方式为csv字典写入，参数1为指定具体文件，参数2为指定字段名
        self.writer = csv.DictWriter(self.f,fieldnames=self.filenames)
        # 写入第一行字段名，因为只要写入一次，所以文件放在_init__里面
        self.writer.writeheader()

    def process_item(self, item, spider):
        print("#########################")
        # 写入spider传过来的具体数据
        self.writer.writerow(item)

        return item

    def close(self,spider):
        self.f.close()
