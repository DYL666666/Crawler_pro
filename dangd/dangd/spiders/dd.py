import scrapy
import time
from ..items import DangdItem
from ..pipelines import DangdPipeline
class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['category.dangdang.com']
    # DangdPipeline.create_dangd_db()
    start_urls = ['http://category.dangdang.com/pg1-cp01.54.06.00.00.00.html']

    def parse(self, response):
        # print(response.text)
        datas=response.xpath(r'//ul[@class="bigimg"]/li')
        # print(datas)
        item=DangdItem()
        for info in datas:
            item['name']=info.xpath(r'./a/@title').extract_first()
            # print(item['name'])
            # id=info.xpath(r'./@id').extract_first()
            # id=id.strip('p')
            # print(id)
            item['price'] = info.xpath(r'.//span[@class="search_now_price"]/text()').extract_first()
            item['or_price'] = info.xpath(r'.//span[@class="search_pre_price"]/text()').extract_first()
            # print(type(item['price']))
            item['author'] = info.xpath(r'.//a[@name="itemlist-author"]/text()').extract_first()
            item['cb_time'] = info.xpath(r'.//p[@class="search_book_author"]/span[2]/text()').extract_first()
            item['cb_time']=item['cb_time'].replace('/','')
            item['cbs'] = info.xpath(r'.//a[@name = "P_cbs"]/text()').extract_first()
            item['comm_num'] = info.xpath(r'.//a[@class="search_comment_num"]/text()').extract_first()
            item['comm_num']=item['comm_num'].strip('条评论')
            item['dp'] = info.xpath(r'.//a[@name="itemlist-shop-name"]/text()').extract_first()
            if not item['dp']:
                item['dp']='当当自营'
            print(item['name'],item['price'],item['or_price'],item['author'],item['cb_time'],item['cbs'],item['comm_num'],item['dp'])
            yield item
        for i in range(2,100):
            url='http://category.dangdang.com/pg{}-cp01.54.06.00.00.00.html'
            yield scrapy.Request(url=url.format(i),callback=self.parse,meta={'item':item})
            time.sleep(2)






