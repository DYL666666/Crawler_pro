# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FirstspiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    teacher=scrapy.Field()
    category=scrapy.Field()
    experience1=scrapy.Field()
    experience2=scrapy.Field()


