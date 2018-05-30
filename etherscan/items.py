# -*- coding: utf-8 -*-

import scrapy

class EtherscanItem(scrapy.Item):
    token_name = scrapy.Field()
    erc20_contract = scrapy.Field()
