# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class EtherscanItem(scrapy.Item):
    token_name = scrapy.Field()
    token_holders = scrapy.Field()
    no_of_transfers = scrapy.Field()
    erc20_contract = scrapy.Field()
