# -*- coding: utf-8 -*-

# Scrapy settings for sdtScrapyProject project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#     http://scrapy.readthedocs.org/en/latest/topics/downloader-middleware.html
#     http://scrapy.readthedocs.org/en/latest/topics/spider-middleware.html
BOT_NAME='SDTSpider'

SPIDER_MODULES=['SDTSpider.spiders']
NEWSPIDER_MODULE='SDTSpider.spiders'

# 并发请求数
#CONCURRENT_REQUESTS=4

# 单个域名并发请求数
CONCURRENT_REQUESTS_PER_DOMAIN=1

# 连续请求时间间隔，单位秒
DOWNLOAD_DELAY=3

# 随机请求时间间隔， (between 0.5 * DOWNLOAD_DELAY and 1.5 * DOWNLOAD_DELAY)
RANDOMIZE_DOWNLOAD_DELAY=True

# 日志文件
LOG_FILE='./SDTSpider.log'

# 日志级别
LOG_LEVEL='DEBUG'

# 用户代理
USER_AGENT='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'

# 重新请求的状态码
RETRY_HTTP_CODES=[500, 502, 503, 504, 408, 429]

# 重新请求的次数
RETRY_TIMES=5


