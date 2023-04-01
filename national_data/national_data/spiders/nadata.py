# import scrapy
#
#
# class NadataSpider(scrapy.Spider):
#     name = 'nadata'
#     allowed_domains = ['data.stats.gov.cn']
#     #start_urls = ['https://data.stats.gov.cn/easyquery.htm?cn=E0103']
#     #start_urls=['https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22310000%22%7D%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A0302%22%7D%5D&k1=1608207507584&h=1']
#     start_urls=["https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22310000%22%7D%5D&dfwds=%5B%7B%22wdcode%22%3A%22zb%22%2C%22valuecode%22%3A%22A0301%22%7D%5D&k1=1608208423545&h=1"]
#     def parse(self, response):
#         text = response.text
#         print(text)
# from time import time
from time import time

import scrapy
from scrapy.http import Response
from jingdong.items import JingdongItem


class ThridSpider(scrapy.Spider):
    name = 'thrid'
    # allowed_domains = ['www.baidu.com']
    start_urls = [
        'https://data.stats.gov.cn/easyquery.htm?m=getOtherWds&dbcode=fsnd&rowcode=zb&colcode=sj&wds=%5B%5D&k1=1608206108278']
    url = 'https://data.stats.gov.cn/easyquery.htm?m=QueryData&dbcode=fsnd&rowcode=zb&colcode=sj&wds=%5B%7B%22wdcode%22%3A%22reg%22%2C%22valuecode%22%3A%22{0}%22%7D%5D&dfwds=%5B%5D&k1={1}'

    def parse_usr(self, response):
        item = response.meta['item']
        page = response.json()

        xx = page['returndata']['datanodes']
        for i in range(len(xx)):
            item['data'] = xx[i]['data']['strdata']
            item['year'] = xx[i]['wds'][2]['valuecode']
            yield item

    def parse(self, response: Response):
        page = response.json()
        xx = page['returndata'][0]['nodes']
        for i in range(len(xx)):
            item = JingdongItem()
            item['code'] = xx[i]['code']
            item['name'] = xx[i]['name']
            times = int(time() * 1000)
            yield scrapy.Request(self.url.format(item['code'], times), callback=self.parse_usr, meta={'item': item})
