# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TonghuashItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class ShFyItem(scrapy.Item):
    ah=scrapy.Field()
    title=scrapy.Field()
    wslb=scrapy.Field()
    ay=scrapy.Field()
    department=scrapy.Field()
    level=scrapy.Field()
    date=scrapy.Field()
class DoubanItem(scrapy.Item):
    score=scrapy.Field()
    cover_x=scrapy.Field()
    title=scrapy.Field()
    url=scrapy.Field()
    cover_y=scrapy.Field()
class HuazpItem(scrapy.Item):
    id=scrapy.Field()
    qy_name=scrapy.Field() #企业名称
    product_id =scrapy.Field()#许可证编号
    product_xm= scrapy.Field()#许可项目
    qy_zs=scrapy.Field()  #企业住所
    qy_address=scrapy.Field()    #生产住址
    shxy_id=scrapy.Field()       #社会信用代码
    fddb_man=scrapy.Field()     #法定代表人
    qyfz_man=scrapy.Field()   #企业负责人
    zlfz_man=scrapy.Field()    #质量负责人
    fzjg = scrapy.Field()#发证机关
    qf_man=scrapy.Field()           #签发人
    daily_jg=scrapy.Field()     #日常监督管理机构
    daily_man=scrapy.Field()    #日常监督管理人员
    yx_time=scrapy.Field()    #有效期至
    fz_time=scrapy.Field()     #发证日期
    state=scrapy.Field()      #状态
    Complaint_hotline=scrapy.Field()#投诉举报电话


