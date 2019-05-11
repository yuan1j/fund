# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from copy import deepcopy

from pymongo import MongoClient


class FundPipeline(object):
    def process_item(self, item, spider):
        mongo = MongoClient()
        collections = mongo["fund"]["monetary_fund"]
        item = deepcopy(item)
        collections.insert(dict(item))
        return item
