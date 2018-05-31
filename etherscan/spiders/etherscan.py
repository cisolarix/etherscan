import re
from scrapy import Spider
from scrapy import Request
from ..items import EtherscanItem

class Etherscan(Spider):
    name = 'etherscan'
    driver = None
    page = 1
    start_urls = [ "https://etherscan.io/tokens" ]

    def start_requests(self):

        # lask_link = response.xpath('//*[@id="ContentPlaceHolder1_divpagingpanel"]/div[2]/p/a[4]/@href').extract()[0]
        # page = response.xpath('//*[@id="ContentPlaceHolder1_divpagingpanel"]/div[2]/p/span/b[2]/text()').extract()[0]
        # range(1, int(page)+1 )

        for inx in range(1, 12): # 手动调整分页数量
            yield Request(
                url='https://etherscan.io/tokens?p={0}'.format(inx),
                meta={'author': 'shooter'},
                callback=self.parse,
                errback=self.error,
            )


    def parse(self, response):
        print("parse url={0}\n, status={1}\n, meta={2}\n".format(response.url, response.status, response.meta ) )

        bodys = response.xpath('//*[@id="ContentPlaceHolder1_divresult"]/table/tbody/tr')

        item = EtherscanItem()

        for i, body in enumerate(bodys):
            title = body.select('./td[3]/h5/a/text()').extract()[0]
            token_link = bodys.xpath('./td[3]/h5/a/@href').extract()[i]

            full_name = title.split("(")[0].strip()   # 全称
            abbr_name = title.split("(")[1][:-1]      # 简称
            erc20_contract = token_link.split('/')[2] # 地址

            item['full_name'] = full_name
            item['abbr_name'] = abbr_name
            item['erc20_contract'] = erc20_contract

            yield item

    def error():
        pass