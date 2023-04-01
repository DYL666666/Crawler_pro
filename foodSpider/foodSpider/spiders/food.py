from typing import Text
import scrapy
from bs4 import BeautifulSoup
from foodSpider.items import FoodspiderItem


class FoodSpider(scrapy.Spider):
    name = 'food'
    allowed_domains = ['https://www.meishij.net']
    start_urls = ['https://www.meishij.net/china-food/caixi/chuancai/?&page=1']

    def parse(self, response):
        text = response.text
        soup = BeautifulSoup(text, 'lxml')
        div_list = soup.select('div.listtyle1_list.clearfix div.listtyle1')
        for div in div_list:
            item = FoodspiderItem()
            item['title'] = div.select('a')[0].get('title')
            item['image_urls'] = [div.select('a img')[0].get('src')]
            yield item
