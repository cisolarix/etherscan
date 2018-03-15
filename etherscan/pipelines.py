# -*- coding: utf-8 -*-

class EtherscanPipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()

    def process_item(self, item, spider):

    def close_spider(self,spider):
        self.session.close()
