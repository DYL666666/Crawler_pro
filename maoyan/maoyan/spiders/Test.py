#-*- codeing = utf-8 -*-
#@Time : 2021/12/27 15:37
#@Author : DYL
#@File : Test.py
#@Software: PyCharm

import scrapy
from bs4 import BeautifulSoup
from maoyan.items import MaoyanItem
import re

# 爬取字段  电影名，主演，上映时间，评分，电影类型，时长，上映地点，累计票房
class maoyan(scrapy.Spider):
    name = "Test"
    allowed_domains = ["www.maoyan.com"]
    start_urls = [
        "https://www.maoyan.com/films/331876"]

    def parse(self,response):
        # print(response.text)
        print(response.status)
        i=0
        if response.status == 200:
            text = response.text
            soup2 = BeautifulSoup(text, 'lxml')
            dt1 = soup2.find_all("div", class_="movie-brief-container")[0]
            dt2 = soup2.find_all("div", class_="movie-stats-container")[0]
            # print(datas)
            # 电影类型
            movie_type = dt1.find_all('li', class_="ellipsis")[0].text.strip()
            print(movie_type)
            # 电影时长
            duration= dt1.find_all('li', class_="ellipsis")[1].text.split("/")[1].strip()  # 时长
            print(duration)
            # 上映地点
            release_place = dt1.find_all('li', class_="ellipsis")[1].text.split("/")[0].strip()  # 上映地点
            print(release_place)
            # 电影票房
            if len(dt2.find_all('div', class_="film-mbox-item")) < 2:
                cumulative_box_office = "暂无"
            else:
                cumulative_box_office = dt2.find_all('div', class_="film-mbox-item")[1].text.strip()  # 累计票房
            print(cumulative_box_office)
