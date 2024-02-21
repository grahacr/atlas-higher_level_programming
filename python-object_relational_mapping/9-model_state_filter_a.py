#!/usr/bin/python3
"""
module to print all states with a in name
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

    """set up engine connection to database"""
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(username, password, db)
    )
    """gather data from engine"""
    Base.metadata.create_all(engine)
    """start session using bind"""
    Session = sessionmaker(bind=engine)
    """create session instance object"""
    session = Session()
    """query returns states filtered by a in the name"""
    a_state = session.query(State).filter(State.name.like('%a%')).order_by(State.id.asc()).all()
    for state in a_state:
        print("{}: {}".format(state.id, state.name))
    """close session"""
    session.close()
