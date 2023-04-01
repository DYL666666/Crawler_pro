import scrapy
# from selenium import webdriver
# form selenium.webdriver.common.by import BY


class TaobaoSpider(scrapy.Spider):
    name = 'Taobao'
    allowed_domains = ['s.taobao.com']
    start_urls = ['https://s.taobao.com/search?q=%E7%AC%94%E8%AE%B0%E6%9C%AC%E7%94%B5%E8%84%91&imgfile=&commend=all&ssid=s5-e&search_type=item&sourceId=tb.index&spm=a21bo.2017.201856-taobao-item.1&ie=utf8&initiative_id=tbindexz_20170306']

    def parse(self, response):
        print(response.text)
        pass
