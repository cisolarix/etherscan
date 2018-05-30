### Etherscan 爬虫

抓取 Etherscan的[Token](https://etherscan.io/tokens)列表

### 使用

1. 安装 Pipenv

`pip install pipenv`

[Pipenv](https://zhuanlan.zhihu.com/p/32913361) 是Python的另一个依赖管理工具

2. 安装依赖包

```shell
pipenv shell   # 激活虚拟环境
pipenv install # 安装
```

3. 运行爬虫 `scrapy crawl etherscan -o token.csv`
