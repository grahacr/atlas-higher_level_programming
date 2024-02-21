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
    state_name = sys.argv[4]

    engine = create_engine(
        f'mysql://{username}: {password}@localhost/{db}'
    )
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)

    session = Session()

    state_ = (
        session.query(State).filter(State.name == state_name).first()
    )
    if state_:
        print("Not found")
    else:
        print(State.id)
    session.close()
