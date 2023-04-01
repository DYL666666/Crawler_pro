import scrapy
from scrapy import Request
from ..items import DoubanItem

class ThsSpider(scrapy.Spider):
    name = 'douban'
    allowed_domains = ['movie.douban.com']
    # url="https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=50&page_start={}"
    # # print([url.format(i)])
    # l=0
    # start_urls = [url.format(0)]

    # pip freeze > requiresment.txt   将依赖包清单导入到requiresment.txt中
    #pip install -r requiresment.txt  将requiresment.txt中依赖包清单读取并下载
    def start_requests(self):
        # 引擎自动爬取10页豆瓣数据
        for page in range(10):
            yield Request(url = f"https://movie.douban.com/j/search_subjects?type=movie&tag=%E7%83%AD%E9%97%A8&sort=recommend&page_limit=50&page_start={page *50}")

    def parse(self, response):
        #print(response.text)
        item=DoubanItem()
        jsdt=response.json()
        jsdt=jsdt['subjects']

        for info in jsdt:
            item['score']=info['rate']
            item['cover_x']=info['cover_x']
            item['title']=info['title']
            item['url']=info['url']
            item['cover_y']=info['cover_y']
            print(self.l)
            self.l=self.l+1
            print(item['score'],item['cover_x'],item['title'],item['url'],item['cover_y'])

        # for i in range(1,6):
        #      print('*'*20)
        #      yield scrapy.Request(url=self.url.format(i*50),callback=self.parse)
