# -*- coding: utf-8 -*-

from .models.config import DBSession
from .models.item import Item

class EtherscanPipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()

    def process_item(self, item, spider):
        # print('------------------')
        # print(item['title'])
        # print('##################')
        i = Item(
                token_holders  = item['title'],
                no_of_transfers         = item['url'],
                erc20_contract       = item['score'],
            )
        self.session.add(i)
        self.session.commit()

    def close_spider(self,spider):
        self.session.close()
