import scrapy


class SuningSpider(scrapy.Spider):
    name = 'suning'
    allowed_domains = ['suning.com']
    start_urls = ['http://snbook.suning.com/web/trd-fl/999999/0.htm']

    def parse(self, response):
        li_list=response.xpath("")
