# Let's propagae some sample data in the 'symbols' table.

from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_module import Symbol, Trade_log  # Import your actual module

# Create an SQLite database in memory (you can adjust this to your actual database)
engine = create_engine('sqlite:///:memory:', echo=True)

# Create the tables
Base.metadata.create_all(engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Initialize Faker
fake = Faker()

# Generate example data
for _ in range(10):  # Create 10 random symbols
    symbol = Symbol(currency_pair=fake.currency_pair())
    session.add(symbol)

session.commit()


