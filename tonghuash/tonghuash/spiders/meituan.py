import scrapy
from scrapy import Request


class MeituanSpider(scrapy.Spider):
    name = 'meituan'
    allowed_domains = ['www.meituan.com']
    start_urls=['https://bj.meituan.com/meishi/api/poi/getPoiList?cityName=%E5%8C%97%E4%BA%AC&cateId=0&areaId=0&sort=&dinnerCountAttrId=&page=1&userId=&uuid=e358121156f341d5a655.1608885180.1.0.0&platform=1&partner=126&originUrl=https%3A%2F%2Fbj.meituan.com%2Fmeishi%2F&riskLevel=1&optimusCode=10&_token=eJxVjk1zqjAUhv9LtjAmNICJO8RSUfFCQdHb6QIDGlDAQCq1nf73m860iztzZt6P8yzeT9D5OZgYCFGEdHArOjABxgiNbKAD2auPjQih1BqPx6alA%2FZ%2FR02qg0O3nYHJC0G2ThB%2B%2FS6eVX4x6APSDUTQq%2F7rsfIPprpvylcQ4FJe%2BwmEh2pUF6V8y5oRa2uofM9LqEYAhdaJQpWefzT7UfmbA7VasX15apQrFsOlYoZ0qseI727cXIY7B%2FOLfzxHbLNwsbd0TgPb993fnfnhxUV%2FokkWuXbp0Xd%2FlWgwQUeeTYPiXq61dj%2F1qEOaje8e8ZESWEHRl9b%2BTlYxXtVDhStXfGyerkZ6X9jBsh2auIZEi25%2BE%2BazIJxvY3bO4nm3R5eZhQWPGObYkXkaijPX0tYqG1%2FsZmJ9CSn%2BE6yvxDb6ebVdVmOYirBl6SZfOfO%2B8IT083ZIheTrwLRcYrXoMTu8J9oUIfYEvv4BY2OJUA%3D%3D']
    def start_requests(self):
        url='https://bj.meituan.com/meishi/api/poi/getPoiList?'
        data={
        'cityName': '北京',
        'cateId': '0',
        'areaId': '0',
        'sort':'',
        'dinnerCountAttrId':'',
        'userId':'',
        'uuid': 'e358121156f341d5a655.1608885180.1.0.0',
        'platform': '1',
        'partner': '126',
        'originUrl': 'https://bj.meituan.com/meishi/pn2/',
        'riskLevel': '1',
        'optimusCode': '10',
        '_token': 'eJx9T9uOokAQ/Zd+ldg3rr6BLoLgBVdYdDIPKsRGFLm0MvRm/317kpmHfdmkknNO1amTqt+g9TMwwQhZCCnglbdgAvAYjXWgAN7JiY5MC1FNo6apK+D8T09FpqaAU5vMwOTNMLBiIvr+2dhK/YYtghSMTPSufHMqOVFlfbp8aQKM87qbQHi6ju95wZ/Hanx+3KHkHStgXREoD/m/Cciw+06GSSy/8PiF/Fsv5V8yqSsulWT5or+JHV5H4kfkrKdG7Tl1jmFfqmlpN78Ctr6oF7+kwzkUV+vQLtaaLYZYtfPcyYnjrBLz485v7kfFlv2x3rmb3hsyPhMOG9HraPQSWvK4BdGMxvFzu2EkmeNpnm5nImF20DVITQOfQBbwUG/lthCP67BnbkUeBEEc1HXqNs7+NV/sD6G3JH0YNLyMtcRUHdddwec5S2lwMA7Rrck2wvD81c8+pKKzp6p1GuAl3xV6Pcxx2r68tGijhPPMGFVlzObgz1+yeJgE'
        }
        # for i in range(2,3):
        #     data['page']=str(i)
        #     yield scrapy.FormRequest(url=url,method='GET',formdata=data,callback=self.parse)
        url1='https://www.meituan.com/meishi/187189334/'
        yield scrapy.Request(url1,callback=self.parse)

    def parse(self, response):
        print(response.text)
