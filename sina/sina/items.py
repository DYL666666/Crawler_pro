# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SinaItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    now_num = scrapy.Field()
    sum_quez = scrapy.Field()
    asymptom_num = scrapy.Field()
    dead_num  = scrapy.Field()
    cure_num   = scrapy.Field()

