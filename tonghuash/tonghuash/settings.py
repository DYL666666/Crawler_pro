# Scrapy settings for tonghuash project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'tonghuash'

SPIDER_MODULES = ['tonghuash.spiders']
NEWSPIDER_MODULE = 'tonghuash.spiders'


# Crawl responsibly by identifying yourself (and your website) on the user-agent
USER_AGENT = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0)'

# Obey robots.txt rules
# ROBOTSTXT_OBEY = True
# LOG_LEVEL='WARN'
# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
# COOKIES_ENABLED = True
# ROBOTSTXT_OBEY=False
# COOKIES_DEBUG = True
# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
# DEFAULT_REQUEST_HEADERS = {
#   'Cookie': 'JSESSIONID=5C0536D815672F8A0DB11A5C19BC50A8-n1',
# 'Host': 'www.hshfy.sh.cn',
# 'Upgrade-Insecure-Requests': 1,
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'
# }
# shfy
# DEFAULT_REQUEST_HEADERS = {
# 'Cookie': 'JSESSIONID=FA4F76158847A7F1017AB367CD9198F1-n1',
# 'Host': 'scxk.nmpa.gov.cn:81',
# 'Origin': 'http://scxk.nmpa.gov.cn:81',
# 'Referer': 'http://scxk.nmpa.gov.cn:81/xk/',
# 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0',
# 'X-Requested-With': 'XMLHttpRequest'}
#huazp
DEFAULT_REQUEST_HEADERS = {
'Cookie': '_lxsdk_cuid=17698e42f8ec8-00958cbe9f934c-c7d6957-1fa400-17698e42f8ec8; uuid=e358121156f341d5a655.1608885180.1.0.0; _lx_utm=utm_source%3Dwww.sogou%26utm_medium%3Dorganic; _lxsdk=17698e42f8ec8-00958cbe9f934c-c7d6957-1fa400-17698e42f8ec8; ci=1; rvct=1%2C151; __mta=156024708.1608885229180.1608885229180.1608885229180.1; client-id=8ee64973-f195-4724-bf7c-6e5062f435e8; _hc.v=727b9b07-b355-ef7f-3216-e6bad99d146d.1608885936; lat=39.98683; lng=116.480639; _lxsdk_s=17699ddb478-9c0-a71-197%7C12%7C12',

'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.81 Safari/537.36 SE 2.X MetaSr 1.0'}
# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'tonghuash.middlewares.TonghuashSpiderMiddleware': 543,
#
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#中间件生效
# DOWNLOADER_MIDDLEWARES = {
#    # 'tonghuash.middlewares.TonghuashDownloaderMiddleware': 543,
# 'tonghuash.middlewares.WangyiproDownloaderMiddleware':551,
#  'tonghuash.middlewares.RandomUserAgent':555
# }

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'tonghuash.pipelines.TonghuashPipeline': 300,
  # 'tonghuash.pipelines.ShfyPipeline':400,
  # 'tonghuash.pipelines.HuazpPipeline':500,
}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'
