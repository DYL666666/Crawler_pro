#-*- codeing = utf-8 -*-
#@Time : 2020/12/20 14:00
#@Author : DYL
#@File : huazp.py
#@Software: PyCharm
import scrapy
import time
from scrapy import Request
from ..items import HuazpItem

class ThsSpider(scrapy.Spider):
    name = 'huazp'
    allowed_domains = ['scxk.nmpa.gov.cn']
    url="http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList"
    # print([url.format(i)])
    start_urls = [url]
    def start_requests(self):
        data={
            'on': 'true',
            'pageSize': '15',
            'productName':'',
            'conditionType': '1',
            'applyname':'',
            'applysn':''
        }
        for i in range(1,362):
            data['page']=str(i);
            yield scrapy.FormRequest(url=self.url,formdata=data,callback=self.parse)
            time.sleep(3)

    def parse(self, response):
        # print(response.text)
        # response=response.text
        item=HuazpItem()
        datas=response.json()
        datas=datas['list']
        #print(datas)
        for info in datas:
            item['id']=info['ID']
            item['qy_name']=info['EPS_NAME']
            item['product_id']=info['PRODUCT_SN']

            item['shxy_id'] = info['BUSINESS_LICENSE_NUMBER']

            item['fzjg'] = info['QF_MANAGER_NAME']

            item['yx_time'] = info['XK_DATE']
            item['fz_time'] = info['XC_DATE']
            # item['state'] = info['']
            item['Complaint_hotline'] = '12331'
            #print(type(item['id']))
            #print(item['id'],item['qy_name'],item['product_id'],item['shxy_id'],item['fzjg'],item['yx_time'],item['fz_time'])
            url="http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById"
            data={}
            data['id']=item['id']
            yield scrapy.FormRequest(url=url,formdata=data,callback=self.get_data,meta={'item':item})
    def get_data(self,response):
        #print(response.text)
        item=response.meta['item']
        dts=response.json()
        item['product_xm']=dts['certStr']
        item['qy_zs']=dts['epsAddress']
        item['qy_address'] = dts['epsProductAddress']
        item['fddb_man'] = dts['legalPerson']
        item['qyfz_man'] = dts['businessPerson']
        item['zlfz_man'] = dts['qualityPerson']
        item['qf_man'] = dts['xkName']
        item['daily_jg'] = dts['rcManagerDepartName']
        item['daily_man'] = dts['rcManagerUser']
        item['state'] = dts['xkType']
        #print(item['id'],item['qy_name'],item['product_id'],item['shxy_id'],item['fzjg'],item['yx_time'],item['fz_time'],item['Complaint_hotline'])
        #print(item['product_xm'], item['qy_zs'],item['qy_address'],item['fddb_man'],item['qyfz_man'],item['zlfz_man'],item['qf_man'],item['daily_jg'],item['daily_man'],item['state'])
        yield item









