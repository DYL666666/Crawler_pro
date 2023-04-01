import scrapy
import re


class A51jobSpider(scrapy.Spider):
    name = '51job'
    allowed_domains = ['www.51job.com']
    start_urls = ['https://search.51job.com/list/190000,000000,0000,00,9,99,python,2,1.html?lang=c&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&ord_field=0&dibiaoid=0&line=&welfare=']

    def parse(self, response):
        print(response.text)
        page_text=response.text
        data=re.findall(r'"attribute_text":(.*?)"companysize_text"',page_text)
        print(data)
        print(page_text)
        data = re.findall(r'"attribute_text":(.*?)"companysize_text"', page_text)
        print(data)
        for it in data:
            td = it[1:-2].split(',')
            area = td[0].replace('"', '')
            if len(td) == 4:
                num = td[3]
            elif len(td) == 3:
                num = td[2]
            else:
                num = td[1]
            num = num.replace('"', '')
            area1 = area.split('-')[0]
            num1 = re.findall(r'招(.*?)人', num)[0]
            if num1 == '若干':
                num1 = 0
            if area1 == '异地招聘':
                area1 = '城市不详'
            print(area1, num1)
            # saveDB(area1,num1)
        item={}
