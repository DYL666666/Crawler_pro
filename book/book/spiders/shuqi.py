import json
import os

import scrapy
from lxml import etree
from scrapy import Request

from book.items import BookItem
from book.pipelines import BookPipeline
import re
import requests

class ShuqiSpider(scrapy.Spider):
    name = 'shuqi'
    allowed_domains = ['www.shuqi.com']
    start_urls = ['https://www.shuqi.com/store?spm=aliwx.index.0.0.6c2b500eCdWd78']

    def parse(self, response):
        # print(response.text)
        item=BookItem()
        file = "E:\pycharm_text\shuqi"
        if not os.path.exists(file):
            os.mkdir(file)
        #/ html / body / div / div[3] / div[2] / ul
        des=re.findall(r'_blank" href="/cover\?(.*?)" class="clear',response.text)
        # print(des)
        url="https://www.shuqi.com/cover?spm=aliwx.list_store.0.0.5d60114bx5gDQl&"
        for i in range(0,len(des)):
            des[i]=url+des[i]
        i=0
        data = response.xpath('//ul[@class="store-ul clear"]/li')
        # print(data.xpath("/html/body/div/div[3]/div[2]/ul/li[1]/a/h3/text()").extract_first())
        for it in data:
            # print(it)
            item["title"] = it.xpath(".//a[@class='clear']/h3/text()").extract_first()
            item["introduction"]=it.xpath("./a/p/text()").extract_first()
            #/ html / body / div / div[3] / div[2] / ul / li[1] / a / p / text()
            item["type"]=it.xpath("./p/span/text()").extract_first()
            item["author"]=it.xpath("./p/a/span/text()").extract_first()
            item["href"]=des[i]
            i=i+1
            print(item)
            yield item
        # for info in des:
        #     # print(info)
        #     yield scrapy.Request(info, callback=self.parse_url)
        #     break

    def parse_url(self,response):
        des_1=response.text
        # print(des_1)
        url1="https://www.shuqi.com/reader?bid=8313723&cid=1376504"
        url="https://www.shuqi.com/reader"
        title=re.findall(r'class="bname">(.*?)</span>',des_1)[0]
        href=re.findall(r' href="/reader(.*?)" data-clog=',des_1)
        href=url+href[0]
        print(title,href)
        yield scrapy.Request(url=href,callback=self.read_book)

    def read_book(self,response):
        des_2=response.text
        # print(des_2)
        title=re.findall(r'<title>(.*?)-书旗网</title>',des_2)[0]
        print(title)
        content=re.findall(r'erName&quot;:&quot;(.*?)}</i>',des_2)
        # print(content.text)
        datas=re.findall(r'ataChapters">(.*?)}</i>',des_2)
        print(datas)
        ds=etree.HTML(datas[0])
        dds=ds.xpath('//text()')
        dds[0].replace('&quot;','')
        print(dds)
        # ds=response.xpath('//i[@class="page-data js-dataChapters"]//text')
        # print(datas,ds)
        # for i in datas:
        #     tt=i.xpath('./span/text()')
        #     print(tt)
        # with open("E:\pycharm_text/shuqi/{}.txt".format(title), "wb") as f:
        #     print("正在下载{}".format(title))
        #     f.write(content)





