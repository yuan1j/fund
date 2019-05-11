# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FundItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    fund_code = scrapy.Field()
    fund_name = scrapy.Field()
    pub_date = scrapy.Field()
    profit_per10000 = scrapy.Field()
    annual_return_7th = scrapy.Field()
    annual_return_14th = scrapy.Field()
    annual_return_28th = scrapy.Field()
    net_value = scrapy.Field()
    rate_1month = scrapy.Field()
    rate_3month = scrapy.Field()
    rate_6month = scrapy.Field()
    rate_1year = scrapy.Field()
    rate_2year = scrapy.Field()
    rate_3year = scrapy.Field()
    rate_5year = scrapy.Field()
    rate_this_year = scrapy.Field()
    rate_all = scrapy.Field()
    fund_company = scrapy.Field()
    fund_manager = scrapy.Field()
    fund_size = scrapy.Field()

