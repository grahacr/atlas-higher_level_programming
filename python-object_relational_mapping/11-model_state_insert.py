#!/usr/bin/python3
"""
module adds new state to database
"""


from sqlalchemy import (create_engine)
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    """set up engine for database"""
    engine = create_engine(
        f'mysql://{username}:{password}@localhost/{db}'
    )
    """gather data from engine"""
    Base.metadata.create_all(engine)
    """start session using bind"""
    Session = sessionmaker(bind=engine)
    """create new session instance"""
    session = Session()
    new_state = State(name='Louisiana')
    print(new_state.id)
    """add new state object to database"""
    session.add(new_state)
    """close session"""
    session.close()
