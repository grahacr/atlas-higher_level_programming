#!/usr/bin/python3
"""
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

    """ """
    engine = create_engine(
        f'mysql://{username}:{password}@localhost/{db}'
    )
    """ """
    Base.metadata.create_all(engine)
    """ """
    Session = sessionmaker(bind=engine)
    session = Session()
    new_state = State(name='Louisiana')
    print(new_state.id)
    session.add(new_state)
    session.close()
