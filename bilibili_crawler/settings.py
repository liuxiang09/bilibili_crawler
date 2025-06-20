# Scrapy settings for bilibili_crawler project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://docs.scrapy.org/en/latest/topics/settings.html
#     https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://docs.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = "bilibili_crawler"

SPIDER_MODULES = ["bilibili_crawler.spiders"]
NEWSPIDER_MODULE = "bilibili_crawler.spiders"

ADDONS = {}


# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = "bilibili_crawler (+http://www.yourdomain.com)"

# Obey robots.txt rules
ROBOTSTXT_OBEY = False  # B站不遵循robots.txt

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://docs.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
DOWNLOAD_DELAY = 2  # 添加延迟，避免被封IP
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
COOKIES_ENABLED = True

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
   "Accept-Language": "zh-CN,zh;q=0.9",
   "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}

# Enable or disable spider middlewares
# See https://docs.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    "bilibili_crawler.middlewares.BilibiliCrawlerSpiderMiddleware": 543,
#}

# Enable or disable downloader middlewares
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html
DOWNLOADER_MIDDLEWARES = {
   "bilibili_crawler.middlewares.BilibiliCrawlerDownloaderMiddleware": 543,
   "bilibili_crawler.middlewares.SeleniumMiddleware": 800,
}

# Enable or disable extensions
# See https://docs.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    "scrapy.extensions.telnet.TelnetConsole": None,
#}

# Configure item pipelines
# See https://docs.scrapy.org/en/latest/topics/item-pipeline.html
#ITEM_PIPELINES = {
#    "bilibili_crawler.pipelines.BilibiliCrawlerPipeline": 300,
#}

# Enable and configure the AutoThrottle extension (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/autothrottle.html
AUTOTHROTTLE_ENABLED = True  # 启用自动限速
# The initial download delay
AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://docs.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = "httpcache"
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = "scrapy.extensions.httpcache.FilesystemCacheStorage"

# Set settings whose default value is deprecated to a future-proof value
FEED_EXPORT_ENCODING = "utf-8"

# -- Selenium相关设置 - 已注释掉，使用Playwright代替 --
SELENIUM_DRIVER_NAME = 'chrome'
# SELENIUM_DRIVER_EXECUTABLE_PATH = "D:\\chromedriver-win64\\chromedriver.exe"
SELENIUM_DRIVER_ARGUMENTS = ['--no-headless', '--start-maximized']

BILIBILI_COOKIES = [
               {
                  "domain": ".bilibili.com",
                  "hostOnly": False,
                  "httpOnly": True,
                  "name": "SESSDATA",
                  "path": "/",
                  "secure": True,
                  "value": "5293d25b%2C1764909930%2C4cb2e%2A61CjBD5u0FJ2lUSrtF0MaAHxnMQI_wFm5FWnrb1Qb-Yz7HxGxNFre0vNUEdFmtrlG3F-ESVllVZEkxOVVSQUR5OWtkWkVfMEZjTV9wMWgyQUtNU1BOb2Z2T0o1NEZ5cTl2bUVnTnNTV0lSQ0daUGl4R2g1TV9maUVLOF9kS0loS1FKRHdZVE9mSDZ3IIEC",
               },
               {
                  "domain": ".bilibili.com",
                  "hostOnly": False,
                  "httpOnly": False,
                  "name": "bili_jct",
                  "path": "/",
                  "secure": False,
                  "value": "a4a51c870475d313181a3ba88a85bf98",
               },
            ]