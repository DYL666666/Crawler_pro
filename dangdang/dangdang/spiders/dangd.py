import scrapy
from ..items import DangdangItem

class DangdSpider(scrapy.Spider):
    name = 'dangd'
    allowed_domains = ['category.dangdang.com']
    for i in range(1,2):
        start_urls = ["http://category.dangdang.com/pg{}-cp01.54.06.00.00.00.html".format(i)]

    def parse(self, response):

        # print(response.text)
        datas=response.xpath(r'//*[@id="component_59"]/li')
        print(response.xpath(r'//*[@id="p29158358"]/div[1]/span/span[1]/text()'))
        item=DangdangItem()
        for info in datas:
            item['name']=info.xpath(r'./a[1]/@title').extract_first()
            # print(item['name'])
            item['author']=info.xpath(r'./p[@class="search_book_author"]/span/a/@title').extract_first()
            item['score']=info.xpath(r'./p[@class="search_star_line"]/span/span/@style').extract_first()
            item['score']=item['score'].strip('width: ').strip('%;')
            item['score']=int(item['score'])/20
            item['price']=info.xpath(r'./p[@class="price"]/span[@class="search_now_price"]/text()').extract_first()
            item['comment_nums']=info.xpath(r'./p[@class="search_star_line"]/a/text()').extract_first()
            item['comment_nums']=item['comment_nums'].strip('条评论')
            item['time']=info.xpath(r'./p[@class="search_book_author"]/span[2]/text()').extract_first()
            item['time']=item['time'].replace('/','')
            item['p_cbs']=info.xpath(r'./p[@class="search_book_author"]/span[3]/a/text()').extract_first()
            #print(item['name'],item['author'],item['score'],item['price'],item['comment_nums'],item['time'],item['p_cbs'])
            yield item

