# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class DangdangItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    price=scrapy.Field()
    author=scrapy.Field()
    score=scrapy.Field()
    comment_nums=scrapy.Field()
    time=scrapy.Field()
    p_cbs=scrapy.Field()
    pass
