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
        'mysql://{}:{}@localhost/{}'.format(username, password, db)
    )
    """ """
    Base.metadata.create_all(engine)
    """ """
    Session = sessionmaker(bind=engine)
    """ """
    session = Session()
    """ """
    a_state = session.query(State).filter(State.name.like('%a%')).order_by(State.id.asc()).all()
    for state in a_state:
        print("{}: {}".format(state.id, state.name))
    session.close()
