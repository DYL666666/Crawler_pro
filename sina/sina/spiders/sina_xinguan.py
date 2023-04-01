import scrapy
import re
from sina.items  import SinaItem

class SinaXinguanSpider(scrapy.Spider):
    name = 'sina_xinguan'
    allowed_domains = ['sina.cn']
    start_urls = ['https://news.sina.cn/zt_d/yiqing0121']

    def parse(self, response):
        print(response.text)
        items=SinaItem()
        datas=re.findall("<div@id='j_tableContent_china'>(.*?)</dir>")
        print(datas)
        #// *[ @ id = "j_tableContent_china"] / div[1]
        data=response.xpath("//*[@id='j_tableContent_china']/ div[1]")
        print(data)
        items["name"]=data.xpath("./span[1]/text()").extract_first()

        for it in data:
           # // *[ @ id = "j_tableContent_china"] / div[1] / span[2]
           items["now_num"] = it.xpath('./span[2]/text()').extract_first()
           # //*[@id="j_tableContent_china"]/div[1]/span[6]
           items["sum_quez"] = it.xpath('./span[3]/text()').extract_first()
           # // *[ @ id = "j_tableContent_china"] / div[1] / span[3] / text()
           items["asymptom_num"] = it.xpath('./span[5]/text()').extract_first()
           # // *[ @ id = "j_tableContent_china"] / div[1] / span[5]
           items["dead_num"] = it.xpath('./span[6]/text()').extract_first()
           # // *[ @ id = "j_tableContent_china"] / div[1] / span[7] / text()
           items["cure_num"] = it.xpath('./span[7]/text()').extract_first()
           print(items)
        pass
