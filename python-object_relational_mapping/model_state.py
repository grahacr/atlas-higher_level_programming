#!/usr/bin/python3
"""
module defines base model connected to mySQL table
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()

class State(Base):
    """subclass inherited from Base
    connects to SQL table called states"""
    __table__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
