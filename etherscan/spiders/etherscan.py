from scrapy import Spider
from scrapy import Request
import re
from ..items import EtherscanItem
from datetime import datetime
import time
from selenium import webdriver


class Etherscan(Spider):
    name = 'etherscan'
    driver = None
    page = 1

    def __init__(self, name=None, **kwargs):
        super().__init__(name, **kwargs)

        chrome_options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(chrome_options=chrome_options)

    def start_requests(self):
        urls = [
            "https://etherscan.io/token/EOS",
            "https://etherscan.io/token/Tronix",
            "https://etherscan.io/token/OmiseGO",
            "https://etherscan.io/token/Qtum",
            "https://etherscan.io/token/ICON",
            "https://etherscan.io/token/BNB",
            "https://etherscan.io/token/DGD",
            "https://etherscan.io/token/Populous",
            "https://etherscan.io/token/Maker",
            "https://etherscan.io/token/StatusNetwork",
            "https://etherscan.io/token/REP",
            "https://etherscan.io/token/ZRX",
            "https://etherscan.io/token/BAT",
            "https://etherscan.io/token/QASH",
            "https://etherscan.io/token/Golem",
            "https://etherscan.io/token/Ethos",
            "https://etherscan.io/token/FunFair",
            "https://etherscan.io/token/Salt",
            "https://etherscan.io/token/KyberNetwork",
            "https://etherscan.io/token/Bancor",
            "https://etherscan.io/token/Request",
            "https://etherscan.io/token/TenXPay",
            "https://etherscan.io/token/ICONOMI",
            "https://etherscan.io/token/Storj",
            "https://etherscan.io/token/Civic",
            "https://etherscan.io/token/Gnosis",
            "https://etherscan.io/token/Monaco",
            "https://etherscan.io/token/Quantstamp",
            "https://etherscan.io/token/Raiden",
            "https://etherscan.io/token/EnjinCoin",
            "https://etherscan.io/token/Aragon",
            "https://etherscan.io/token/Decentraland",
            "https://etherscan.io/token/RLC",
            "https://etherscan.io/token/SAN",
            "https://etherscan.io/token/Metal",
            "https://etherscan.io/token/Edgeless",
            "https://etherscan.io/token/RipioCreditNetwork",
            "https://etherscan.io/token/Amber",
            "https://etherscan.io/token/AirSwap",
            "https://etherscan.io/token/WINGS",
            "https://etherscan.io/token/Melon",
            "https://etherscan.io/token/TAAS",
            "https://etherscan.io/token/SNGLS",
            "https://etherscan.io/token/CoinDash",
            "https://etherscan.io/token/district0x",
            "https://etherscan.io/token/Lunyr",
            "https://etherscan.io/token/BCAP",
            "https://etherscan.io/token/Humaniq",
            "https://etherscan.io/token/AdToken",
            "https://etherscan.io/token/TokenCard",
            "https://etherscan.io/token/Cofoundit",
            "https://etherscan.io/token/Numeraire",
            "https://etherscan.io/token/NimiqNetwork",
            "https://etherscan.io/token/Trustcoin",
            "https://etherscan.io/token/Guppy",
            "https://etherscan.io/token/FirstBlood",
            "https://etherscan.io/token/TIME",
            "https://etherscan.io/token/SwarmCity",
            "https://etherscan.io/token/Xaurum",
            "https://etherscan.io/token/Pluton",
            "https://etherscan.io/token/DICE",
            "https://etherscan.io/token/HelloGold",
            "https://etherscan.io/token/vSlice",
            "https://etherscan.io/token/Indorse",
            "https://etherscan.io/token/FundYourselfNow",
        ]

        for url in urls:
            self.logger.info('starting .....')
            request = Request(url=url, callback=self.parse)
            yield request

    def parse(self, response):
        item = EtherscanItem()

        erc20_contract = response.xpath('//*[@id="ContentPlaceHolder1_trContract"]/td[2]/a/text()').extract()[0]
        token_name = response.xpath('//*[@id="address"]/text()').extract()[0]

        item['token_name'] = token_name
        item['erc20_contract'] = erc20_contract

        yield item

    @staticmethod
    def close(spider, reason):
        spider.driver.quit()
        return super().close(spider, reason)
