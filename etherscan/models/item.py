from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Item(Base):
    __tablename__ = 'items'

    id              = Column(Integer, primary_key=True)
    token_holders   = Column(String)
    no_of_transfers = Column(String)
    erc20_contract  = Column(String)
