#!/usr/bin/python3
"""
This module defines a State class and an instance Base using SQLAlchemy's declarative_base.

State class:
- Inherits from Base
- Links to the MySQL table 'states'
- Has class attributes:
  - id: represents a column of an auto-generated, unique integer, can't be null and is a primary key
  - name: represents a column of a string with maximum 128 characters and can't be null

The script connects to a MySQL server running on localhost at port 3306.
"""

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Create an instance of the declarative_base
Base = declarative_base()

class State(Base):
    """
    State class that links to the MySQL table 'states'.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

if __name__ == "__main__":
    # Replace with your MySQL username, password, and database name
    username = 'your_username'
    password = 'your_password'
    dbname = 'hbtn_0e_6_usa'

    # Create an engine that stores data in the local directory's
    # hbtn_0e_6_usa database.
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}', echo=True)

    # Create all tables in the engine by calling the metadata's create_all method
    Base.metadata.create_all(engine)
