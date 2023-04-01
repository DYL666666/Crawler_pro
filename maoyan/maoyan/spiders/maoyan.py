#-*- codeing = utf-8 -*-
#@Time : 2021/12/27 12:51
#@Author : DYL
#@File : maoyan.py
#@Software: PyCharm
import random
import time


import scrapy
from bs4 import BeautifulSoup
from maoyan.items import MaoyanItem
import re

# 爬取字段  电影名，主演，上映时间，评分，电影类型，时长，上映地点，累计票房
class maoyan(scrapy.Spider):
    name = "maoyan"
    allowed_domains = ["www.maoyan.com"]
    start_urls = [
        "https://www.maoyan.com/films?isPlay=1&showType=3&offset={}".format(
            str(i * 30))
        for i in range(0,57)]

    def parse(self,response):
        # print(response.text)
        if response.status == 200:
            text = response.text
            soup1 = BeautifulSoup(text, 'lxml')
            dd_list = soup1.find_all("dd")
            # print(dd_list)
            for dts in dd_list:
                item = MaoyanItem()
                all_dts = dts.find_all("div",attrs={'class':"movie-hover-info"})[0]
                # 随机生成用户id
                item['user_id'] = random.randrange(100, 601, 1)
                # print(item['user_id'])
                # 电影名
                item['movie_name'] = all_dts.find_all("span",attrs={'class':"name"})[0].text.strip()
                # print(item['movie_name'])
                # 主演
                item['actors'] = all_dts.find_all("div",class_="movie-hover-title")[2].text.strip("主演:\n").strip()
                # print(item['actors'])
                # 上映时间
                item['release_time'] = all_dts.find_all("div",class_="movie-hover-title movie-hover-brief")[0].text.strip("上映时间:\n").strip()
                # print(item['release_time'])
                # 评分
                item['score'] =dts.find_all("div",class_="channel-detail channel-detail-orange")[0].text.strip()
                # print(item['score'])
                # url
                url = dts.find_all("a",attrs={"data-act":"movie-click"})[0].attrs["href"]
                item['movie_id'] = url.split('/')[2]
                url = "https://www.maoyan.com"+url
                # print(url)
                yield scrapy.Request(url=url,callback=self.get_data,meta={'item':item})# dont_filter=True
        else:
            return

    def get_data(self,response):
        # print(response.text)
        item = response.meta['item']
        if response.status == 200:
            text = response.text
            soup2 = BeautifulSoup(text,'lxml')
            print("爬取的实际链接："+response.url)
            dt1 = soup2.find_all("div",class_="movie-brief-container")[0]
            dt2 = soup2.find_all("div",class_="movie-stats-container")[0]
            # print(datas)
            # 电影类型
            item['movie_type'] = dt1.find_all('li',class_="ellipsis")[0].text.strip().replace('\n','/').strip()
            # print(item['movie_type'])
            # 电影时长
            item['duration'] = dt1.find_all('li',class_="ellipsis")[1].text.split("/")[1].strip()# 时长
            # print(item['duration'])
            # 上映地点
            item['release_place'] = dt1.find_all('li',class_="ellipsis")[1].text.split("/")[0].strip()# 上映地点
            # print(item['release_place'])
            # 电影票房
            mlen =  len(soup2.find_all('div',class_="film-mbox-item"))
            if mlen <2:
                item['cumulative_box_office'] ="暂无"
            else:
                item['cumulative_box_office'] =soup2.find_all('div',class_="film-mbox-item")[mlen - 1].text.strip().replace('\n累计票房','') # 累计票房
            print(item)
            time.sleep(3)
            yield item
        else:
            return

