# -*- coding: utf-8 -*-
import scrapy
from fund.items import FundItem


class MonetaryFundSpider(scrapy.Spider):
    name = 'monetary_fund'
    allowed_domains = ['eastmoney.com']
    start_urls = ['http://fund.eastmoney.com/data/hbxfundranking.html#t;c0;r;sTEYI;ddesc;pn50;mg;os1;']

    def parse(self, response):
        # 获取item对象
        item = FundItem()
        # 分组
        tr_list = response.xpath('//table[@id="dbtable"]/tbody/tr')
        print(tr_list)
        # 　遍历
        for tr in tr_list:
            item["fund_code"] = tr.xpath("./td[3]/a/text()").extract_first()
            item["fund_name"] = tr.xpath("./td[4]/a/text()").extract_first()
            item["pub_date"] = tr.xpath("./td[5]/text()").extract_first()
            item["profit_per10000"] = tr.xpath("./td[6]/text()").extract_first()
            item["annual_return_7th"] = tr.xpath("./td[7]/text()").extract_first()
            item["annual_return_14th"] = tr.xpath("./td[8]/text()").extract_first()
            item["annual_return_28th"] = tr.xpath("./td[9]/text()").extract_first()
            item["net_value"] = tr.xpath("./td[10]/text()").extract_first()
            item["rate_1month"] = tr.xpath("./td[11]/text()").extract_first()
            item["rate_3month"] = tr.xpath("./td[12]/text()").extract_first()
            item["rate_6month"] = tr.xpath("./td[13]/text()").extract_first()
            item["rate_1year"] = tr.xpath("./td[14]/text()").extract_first()
            item["rate_2year"] = tr.xpath("./td[15]/text()").extract_first()
            item["rate_3year"] = tr.xpath("./td[16]/text()").extract_first()
            item["rate_5year"] = tr.xpath("./td[17]/text()").extract_first()
            item["rate_this_year"] = tr.xpath("./td[18]/text()").extract_first()
            item["rate_all"] = tr.xpath("./td[19]/text()").extract_first()

            url_detail = tr.xpath("./td[4]/a/@href").extract_first()
            # print(item["fund_code"])
            print(item["fund_name"])
            # print(url_detail)
            yield scrapy.Request(url_detail, callback=self.parse_detail, meta={"item": item})

        # 构造下一页url
        # if response.xpath('//div[@id="pagebar"]/label[last()]/@class').extract_first() != "end":
        #     next_url = response.xpath('//div[@id="pagebar"]/label[last()]/text()').extract_first()
        #     yield scrapy.Request(next_url)


    def parse_detail(self, response):
        item = response.meta["item"]
        item["fund_size"] = response.xpath('//div[@class="infoOfFund"]/table/tr[1]/td[2]/a/text()').extract_first()
        item["fund_manager"] = response.xpath('//div[@class="infoOfFund"]/table/tr[1]/td[3]/a/text()').extract_first()
        item["fund_company"] = response.xpath('//div[@class="infoOfFund"]/table/tr[2]/td[2]/a/text()').extract_first()
        yield item
