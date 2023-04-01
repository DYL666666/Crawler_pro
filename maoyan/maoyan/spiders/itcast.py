import scrapy


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.com']
    start_urls = ['http://itcast.com/']

    def parse(self, response):
        print()
