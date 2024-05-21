from sqlalchemy import Column, Float, Integer, String, Table, ForeignKey, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime

now = datetime.now()
print(f"Current date and time: {now}")

Base = declarative_base()
engine = create_engine('sqlite+pysqlite:///trade_tracker.db')

class Symbol(Base):
    __tablename__ = 'symbol'
    id = Column(Integer, primary_key=True)
    currency_pair = Column(String, unique=True)  # Example: 'USD/EUR'
    trades = relationship('Trade', back_populates='symbol')


# Create all tables
Base.metadata.create_all(engine)