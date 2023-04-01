import time
from time import sleep

import scrapy
from ..items import ShFyItem

class ThsSpider(scrapy.Spider):
    name = 'shfy'
    allowed_domains = ['data.10jqka.com.cn']
    url="http://www.hshfy.sh.cn/shfy/gweb2017/flws_list.jsp?ajlb=aYWpsYj3D8crCz"
    start_urls = ["http://www.hshfy.sh.cn/shfy/gweb2017/flws_list_content_c.jsp"]
    def start_requests(self):
        data={
            'fydm': '',
            'ah': '',
            'ay': '',
            'ajlb': '%E6%B0%91%E4%BA%8B',
            'wslb': '',
            'title': '',
            'jarqks': '',
            'jarqjs': '',
            'qwjs': '',
            'wssj': '',
            'yg': '',
            'bg': '',
            'spzz': '',
            'flyj': '',
            'zbah': ''
        }
        for i in range(1,5):
            data['pagesnum']=str(i);
            print("start_requests  ",i)

            yield scrapy.FormRequest(url=self.start_urls[0],formdata=data,callback=self.parse)
            time.sleep(6)


    def parse(self, response):
        # print(response.text)
        item=ShFyItem()
        datas=response.xpath(r'//table[@class="sTable"]/tr')
        flag=True
        for info in datas:
            if flag:
                flag=False
                continue
            item['ah'] =info.xpath(r'./td[1]/text()').extract_first()
            item['title'] =info.xpath(r'./td[2]/text()').extract_first()
            item['wslb'] =info.xpath(r'./td[3]/text()').extract_first()
            item['ay'] =info.xpath(r'./td[4]/text()').extract_first()
            item['department'] =info.xpath(r'./td[5]/text()').extract_first()
            item['level'] =info.xpath(r'./td[6]/text()').extract_first()
            item['date'] =info.xpath(r'./td[7]/text()').extract_first()
            print(item['ah'],item['title'],item['wslb'],item['ay'],item['department'],item['level'],item['date'])
            yield item
