import json

import scrapy
from scrapy.http import Request
from firstspider.items import FirstspiderItem
from firstspider.pipelines import FirstspiderPipeline

def process_item(self, item, spider):
    pass


class ItcastSpider(scrapy.Spider):
    name = 'itcast'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml#']

    def parse(self, response):
        print(response)
        ul_list=response.xpath("//ul[@class='clears']/li")
        ul_list=response.xpath("/html/body/div[10]/div/div[2]/ul/li")
        print(ul_list)
        #/ html / body / div[10] / div / div[2] / ul / li[1] / div[2] / h2 / text()
        #/ html / body / div[10] / div / div[2] / ul / li[1] / div[2] / h3 / span[2]
        item=FirstspiderItem()
        for it in ul_list:
             item["teacher"]=it.xpath("./div[2]/h2/text()").extract_first()
             item["category"]=it.xpath("./div[2]/h2/span/text()").extract_first()
             item["experience1"]=it.xpath("./div[2]/h3/span[1]/text()").extract_first()
             item["experience2"] = it.xpath("./div[2]/h3/span[2]/text()").extract_first()
             if item["experience2"]==None:
                 pass
             print(item)
             yield item
        item1=[]
        # ul_list1=response.xpath("//div[@class='fdnav']/ul/li")
        # url=ul_list1.xpath("./a/@href").extract_first()
        # print(ul_list1)
        # print(url)
        # if url:
        #     print("Request:")
        #     yield Request(url, callback=self.parse())
        # return item


