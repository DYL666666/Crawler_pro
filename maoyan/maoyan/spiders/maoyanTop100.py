#-*- codeing = utf-8 -*-
#@Time : 2021/11/24 9:28
#@Author : DYL
#@File : maoyanTop100.py
#@Software: PyCharm

import scrapy
from bs4 import BeautifulSoup
from maoyan.items import MaoyanItem
import re

# 爬取字段  电影名，主演，上映时间，评分，电影类型，时长，上映地点，累计票房
class maoyan(scrapy.Spider):
    name = "maoyanTop100"
    allowed_domains = ["www.maoyan.com"]
    # start_urls = ["https://www.maoyan.com/board/4?timeStamp=1637717213525&sVersion=1&offset={}&index=2&signKey=23d67d4e0b2788f0230fca975d057561&channelId=40011&requestCode=b5b4692661fde0cfe6e76abc6ed27248gnbyo".format(str(i*10))
    #        for i in range(3,5)]
    start_urls = [
        "https://www.maoyan.com/films?isPlay=1&showType=3&offset={}".format(
            str(i * 30))
        for i in range(0, 1)]

    def parse(self,response):
        # print(response.text)
        text = response.text
        soup1 = BeautifulSoup(text, 'lxml')
        dd_list = soup1.find_all("dd")
        print(dd_list)
        for dts in dd_list:
            item = MaoyanItem()
            # 电影名
            item['movie_name'] = dts.find_all("p",attrs={'class':"name"})[0].text.strip()
            print(item['movie_name'])
            # 主演
            item['actors'] = dts.find_all("p",class_="star")[0].text.strip()
            print(item['actors'])
            # 上映时间
            item['release_time'] = dts.find_all("p",class_="releasetime")[0].text.strip()
            print(item['release_time'])
            # 评分
            item['score'] =dts.find_all("p",class_="score")[0].text.strip()
            print(item['score'])
            # url
            url = dts.find_all("a",class_="image-link")[0].attrs["href"]
            url = "https://www.maoyan.com"+url
            print(url)
            yield scrapy.Request(url=url,callback=self.get_data,meta={'item':item})# dont_filter=True
    def get_data(self,response):
        # print(response.text)
        text = response.text
        item = response.meta['item']
        soup2 = BeautifulSoup(text,'lxml')
        datas = soup2.find_all("div",class_="celeInfo-right clearfix")[0]
        # print(datas)
        item['movie_type'] = datas.find_all('li',class_="ellipsis")[0].text.strip()
        # print(item['movie_type'])
        item['duration'] = datas.find_all('li',class_="ellipsis")[1].text.split("/")[1].strip()# 时长
        # print(item['duration'])
        item['release_place'] = datas.find_all('li',class_="ellipsis")[1].text.split("/")[0].strip()# 上映地点
        # print(item['release_place'])
        if len(soup2.find_all('div',class_="film-mbox-item")) <2:
            item['cumulative_box_office'] ="暂无"
        else:
            item['cumulative_box_office'] =soup2.find_all('div',class_="film-mbox-item")[1].text.strip() # 累计票房
        print(item)
        # yield item





