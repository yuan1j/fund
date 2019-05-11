# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import time

from scrapy import signals
from scrapy.http import HtmlResponse
from selenium import webdriver


class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Chrome()

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(5)
        source = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url, body=source, request=request, encoding="utf8")
        return response
