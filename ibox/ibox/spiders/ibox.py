#-*- codeing = utf-8 -*-
#@Time : 2022/8/10 11:02
#@Author : DYL
#@File : ibox.py
#@Software: PyCharm

import scrapy

class IboxSpider(scrapy.Spider):
    name = 'ibox'
    allowed_domains = ['ibox.art']
    start_urls = ['https://www.ibox.art/zh-cn/']

    def parse(self, response):
        print(response.text)

