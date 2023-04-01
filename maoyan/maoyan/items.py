# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

# 爬取字段  电影名，主演，上映时间，评分，电影类型，时长，上映地点，累计票房
class MaoyanItem(scrapy.Item):
    # define the fields for your item here like:
    user_id = scrapy.Field() #用户id
    movie_id = scrapy.Field() #电影id
    movie_name = scrapy.Field()  # 电影名
    actors = scrapy.Field()  # 主演
    release_time = scrapy.Field()  # 上映时间
    score = scrapy.Field()  # 评分
    movie_type = scrapy.Field()  # 电影类型
    duration = scrapy.Field()  # 时长
    release_place = scrapy.Field()  # 上映地点
    cumulative_box_office = scrapy.Field()  # 累计票房
