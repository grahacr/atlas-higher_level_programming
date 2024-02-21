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
    state_update = session.query(State).filter(State.id == '2').first()
    if state_update:
        state_update.name = 'New Mexico'
        session.commit()
    session.close()
