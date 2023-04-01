import scrapy


class MeishijSpider(scrapy.Spider):
    name = 'meishij'
    allowed_domains = ['www.meishij.net']
    start_urls = ['https://www.meishij.net/zuofa/ganbiansijidou_37.html']

    def parse(self, response):
        print(response.text)

