# -*- coding: utf-8 -*-

import scrapy

class EtherscanItem(scrapy.Item):
    token_name = scrapy.Field()
    token_holders = scrapy.Field()
    no_of_transfers = scrapy.Field()
    erc20_contract = scrapy.Field()
