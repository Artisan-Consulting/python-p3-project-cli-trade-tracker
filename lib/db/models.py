from sqlalchemy import Column, Float, Integer, String, Table, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime
from sqlalchemy import Numeric


#now = datetime.now()
#print(f"Current date and time: {now}")

Base = declarative_base()
engine = create_engine('sqlite+pysqlite:///trade_data.db')

class Symbol(Base):
    __tablename__ = 'symbols'
    id = Column(Integer, primary_key=True)
    currency_pair = Column(String, unique=True)  # Example: 'USD/EUR'
    trades = relationship('Trade', back_populates='symbol')

class Trade(Base):
    __tablename__ = 'trade_log'
    id = Column(Integer, primary_key=True)
    symbol_id = Column(Integer, ForeignKey('symbol.id'))
    symbol = relationship(Symbol, back_populates='trades')
    buysell = Column(String, default='Sell')
    lot_size = Column(Integer)
    #entry_date_time = Column(DateTime, default=func.now())
    #exit_date_time = Column(DateTime, default=None)
    entry_price = Column(Numeric(precision=10, scale=6))  # 6 decimal places
    exit_price = Column(Numeric(precision=10, scale=6))  # 6 decimal places

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True)
    account_number = Column(String, unique=True)
    trades = relationship('Trade', back_populates='account')

# Create all tables
Base.metadata.create_all(engine)