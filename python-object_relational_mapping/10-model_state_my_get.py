#!/usr/bin/python3
"""
module for printing state object associated with given name
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
    state_name = sys.argv[4]

    """set up engine connection to database"""
    engine = create_engine(
        f'mysql://{username}:{password}@localhost/{db}'
    )
    """gather data from engine"""
    Base.metadata.create_all(engine)
    """start session using bind"""
    Session = sessionmaker(bind=engine)
    """create session instance of object"""
    session = Session()
    """query returns state object if matching argument passed"""
    state_ = (
        session.query(State).filter(State.name == state_name).first()
    )
    if state_:
        print("Not found")
    else:
        print(State.id)
    """close session"""
    session.close()
