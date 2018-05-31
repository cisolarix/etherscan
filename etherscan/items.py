# -*- coding: utf-8 -*-

import scrapy

class EtherscanItem(scrapy.Item):
    full_name = scrapy.Field()
    abbr_name = scrapy.Field()
    erc20_contract = scrapy.Field()
