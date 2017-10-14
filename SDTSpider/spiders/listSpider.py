# -*- coding: utf-8 -*-
import scrapy
import time
import re


class ListspiderSpider(scrapy.Spider):
    name = "listSpider"
    allowed_domains = ["autohome.com.cn"]
    start_urls = [('http://club.autohome.com.cn/bbs/forum-o-200042-%d.html' % i) for i in xrange(1, 2)]

    def parse(self, response):
        for item in response.css('div#subcontent dl.list_dl:not(.bluebg)'):
            link = response.urljoin(item.css('a.a_topic::attr(href)').extract_first()) or ''
            yield response.follow(link.replace('thread', 'threadowner'), self.parse_detail)

    def parse_detail(self, response):
        html_name = response.url.split('/')[-1]
        file_name = self.get_file_name(html_name)
        mode = 'w' if self.is_first_page(html_name) else 'a'
        with open(file_name, mode) as f:
            f.write('\n'.join(response.xpath(
                '//div[@class="conttxt"]/div[@class="w740"]/div//text()').extract()).encode('utf8'))

        next_page = response.css('a.afpage::attr(href)').extract_first()
        if next_page != None:
            yield response.follow(next_page, self.parse_detail)

    def transcode(self, str):
        if str is None:
            return str
        else:
            return str.encode('utf8')

    def is_first_page(self, html_name):
        return re.match('.*1\.html$', html_name) != None

    def get_file_name(self, html_name):
        return './html_file/' + '-'.join(html_name.split('-')[2:-1]) + '.html'
