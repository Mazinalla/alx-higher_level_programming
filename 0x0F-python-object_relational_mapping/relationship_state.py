#!/usr/bin/python3
"""
Defines the State class and Bla bla bla
.
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from relationship_city import Base


'''
    Bla bla bla
'''
class State(Base):
    """State class."""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", back_populates="state", cascade="all, delete")
