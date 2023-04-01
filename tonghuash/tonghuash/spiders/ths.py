import scrapy
from scrapy import Request


class ThsSpider(scrapy.Spider):
    name = 'ths'
    allowed_domains = ['data.10jqka.com.cn']
    url="http://data.10jqka.com.cn/market/zdfph/agentSource/static1608271813/field/zdf/order/desc/ajax/1/free/1/page/{}/free/1/"
    # print([url.format(i)])
    start_urls = [url.format(3)]
    def start_requests(self):
        url="http://data.10jqka.com.cn/market/zdfph/agentSource/static1608271813/field/zdf/order/desc/ajax/1/free/1/page/{}/free/1/"
        headers={
            'User - Agent': 'Mozilla / 5.0(Windows NT 10.0;WOW64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 72.0.3626.81Safari / 537.36SE2.XMetaSr1.0',
        'Host': 'data.10jqka.com.cn',
            'Upgrade - Insecure - Requests': '1',
            'Accept': 'text/html,application/xhtml + xml,application/xml;q = 0.9,image/webp,image/apng, * / *;q = 0.8',
        'Accept - Encoding': 'gzip, deflate',
        'Accept - Language': 'zh - CN, zh;q = 0.9',
        'Cache - Control': 'max - age = 0',
        'Connection': 'keep - alive',
        }
        cookies={
            'Hm_lvt_f79b64788a4e377c608617fba4c736e2' :'1608271587, 1608342282',
        'Hm_lvt_60bad21af9c824a4a0530d5dbf4357ca' : '1608271586, 1608342282',
        'Hm_lvt_78c58f01938e4d85eaf619eae71b4ed1' :'1608271587, 1608342282',
        'v' : 'Ao_QVrDPDFuG8QinfKftOh - XHiiKtOPWfQjnyqGcK_4FcKHUqYRzJo3Ydxay'      }
        print("start_requests")
        yield Request(url=url.format(1),headers=headers,cookies=cookies,callback=self.parse)

    def parse(self, response):
        print(response.text)
        datas=response.xpath(r'//*[@id="J-ajax-main"]/table/tbody/tr')
        for info in datas:
            dts=info.xpath(r'.//text()')
            print(dts)
        # print(datas)

        # yield scrapy.Request(url=self.url.format(2),callback=self.parse)
