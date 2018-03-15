from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# 初始化数据库连接:
engine = create_engine('mysql+pymysql://root:''@localhost/douban_spiders?charset=utf8')

# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)
