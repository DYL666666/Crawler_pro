# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price = scrapy.Field()
    or_price= scrapy.Field()
    author= scrapy.Field()
    cb_time= scrapy.Field()
    cbs= scrapy.Field()
    comm_num= scrapy.Field()
    dp= scrapy.Field()
