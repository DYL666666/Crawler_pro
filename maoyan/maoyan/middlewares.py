# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals

# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MaoyanSpiderMiddleware:
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


class MaoyanDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.

    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.
        request.cookies = {
            "__mta": "108886461.1637716594485.1637719534066.1637722552530.16",
            "_lxsdk_cuid": "17d4f840f01c8-0b378b76791186-59191353-144000-17d4f840f01c8",
            "uuid_n_v": "v1",
            "uuid": "6A5A8050686E11EC87FF41B5867757986E4BD2435F224C4788079371C72CD725",
            "_csrf": "04e20eaa4286387f46080cbfa2270cfd859f7504f32fc2789b71d53e1f96ae78",
            "Hm_lvt_703e94591e87be68cc8da0da7cbd0be2": "1640758401",
            "_lx_utm": "utm_source%3Dbing%26utm_medium%3Dorganic",
            "_lxsdk": "6A5A8050686E11EC87FF41B5867757986E4BD2435F224C4788079371C72CD725",
            "Hm_lpvt_703e94591e87be68cc8da0da7cbd0be2": "1640771281",
            "__mta": "108886461.1637716594485.1637722552530.1640771281988.17",
            "_lxsdk_s": "17e0530beca-aab-2eb-8e7%7C%7C81"
        }
        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response


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
