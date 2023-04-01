# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from scrapy.http import HtmlResponse


# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from scrapy.http.response.html import HtmlResponse
from scrapy.http.response.text import TextResponse
from selenium.webdriver import ActionChains

class WangyiDownloaderMiddleware(object):
    def __init__(self):
        self.browser = create_chrome_driver(headless = True)
        self.browser.get("https://")#此处填要爬取的网站ip
        add_cookies(self.browser,'taobao.json')
    def __del__(self):
        self.browser.close()
    # 可以拦截到request请求
    def process_request(self,request,spider):
        # 在进行url访问之前可以进行的操作, 更换UA请求头, 使用其他代理等
        # request.cookies = COOKIES_DICT
        # request.meta{"proxy":'http://1.2.3.4:1086'} ip代理

        self.browser.get(request.url)
        # body= self.browser.page_source抓取动态页面
        return HtmlResponse(url= request.url,body= self.browser.page_source,
                            request= request, encoding= 'utf-8')
        pass
    def process_response(selfself,request,response,spider):
        """ 三个参数:
               # request: 响应对象所对应的请求对象
               # response: 拦截到的响应对象
               # spider: 爬虫文件中对应的爬虫类 WangyiSpider 的实例对象, 可以通过这个参数拿到 WangyiSpider 中的一些属性或方法
               """
        if request.url in ['http://news.163.com/domestic/","http://war.163.com/","http://news.163.com/world/","http://news.163.com/air/']:
            spider.browser.get(url=request.url)
            # more_btn = spider.browser.find_element_by_class_name("post_addmore")     # 更多按钮
            # print(more_btn)
            js="window.scrollTo(0,document.body.scrollHeight)"
            spider.browser.execute_script(js)
            # if more_btn and request.url == "http://news.163.com/domestic/":
            #     more_btn.click()
            time.sleep(1)# 等待加载,  可以用显示等待来优化.
            row_response=spider.browser.page_source
            return HtmlResponse(url=spider.browser.current_url,body=row_response,encoding='utf8',request=request)
        else:
            return response# 是原来的主页的响应对象
    def process_exception(self,request,exception,spider):
        print("添加代理开始")
        re_proxy=get_proxy()
        request.meta['proxy']=ret_proxy
        print("为%s添加代理%s"%(request.url,ret_proxy),end="")
        return None
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
]
class RandomUserAgent(UserAgentMiddleware):
    def process_request(self,request,spider):
        ua=random.choice(user_agent_list)
        request.headers.setdefault("User-Agent",ua)
class TaobaoMiddleware(object):

    # 处理请求函数
    def process_request(self, request, spider):
        # 声明一个Options对象
        opt = Options()
        # 给对象添加一个--headless参数,表示无头启动
        opt.add_argument('--headless')
        # 把配置参数应用到驱动创建的对象
        driver = webdriver.Chrome(options=opt)
        # 打开requests中的地址
        driver.get(request.url)

        # 让浏览器滚动到底部
        for x in range(1, 11):
            j = x / 10
            js = "document.documentElement.scrollTop = document.documentElement.scrollHeight*%f" % j
            driver.execute_script(js)
            # 每次滚动等待0.5s
            time.sleep(5)

        # 获取下一页按钮的标签
        next_btn = driver.find_element_by_xpath('//span[contains(text(),"下一页")]')
        # 睡眠0.5秒
        time.sleep(0.5)
        # 对下一页标签进行鼠标右键触发事件
        ActionChains(driver).context_click(next_btn).click().perform()
        # driver.save_screenshot('截图.png')
        # 把驱动对象获得的源码赋值给新变量
        page_source = driver.page_source
        # 退出
        driver.quit()

        # 根据网页源代码,创建Htmlresponse对象
        response = HtmlResponse(url=request.url, body=page_source, encoding='utf-8', request=request)
        # 因为返回的是文本消息,所以需要指定字符编码格式

        return response

    def process_response(self, request, response, spider):
        return response

    def process_exception(self, request, exception, spider):
        pass
class TonghuashSpiderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the spider middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_spider_input(self, response, spider):
        # Called for each response that goes through the spider
        # middleware and into the spider.

        # Should return None or raise an exception.
        return None

    def process_spider_output(self, response, result, spider):
        # Called with the results returned from the Spider, after
        # it has processed the response.

        # Must return an iterable of Request, or item objects.
        for i in result:
            yield i

    def process_spider_exception(self, response, exception, spider):
        # Called when a spider or process_spider_input() method
        # (from other spider middleware) raises an exception.

        # Should return either None or an iterable of Request or item objects.
        pass

    def process_start_requests(self, start_requests, spider):
        # Called with the start requests of the spider, and works
        # similarly to the process_spider_output() method, except
        # that it doesn’t have a response associated.

        # Must return only requests (not items).
        for r in start_requests:
            yield r

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)


class TonghuashDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_request(self, request, spider):
        # Called for each request that goes through the downloader
        # middleware.

        # Must either:
        # - return None: continue processing this request
        # - or return a Response object
        # - or return a Request object
        # - or raise IgnoreRequest: process_exception() methods of
        #   installed downloader middleware will be called
        return None

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response

    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
