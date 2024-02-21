#!/usr/bin/python3
"""
module to print first state object in database
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

    """create engine and connect to database"""
    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(username, password, db)
    )
    """retrieve data for use"""
    Base.metadata.create_all(engine)
    """use bind function to bind engine to session"""
    Session = sessionmaker(bind=engine)
    """create session instance"""
    session = Session()
    """query and print results of first state stored in variable"""
    first_state = session.query(State).order_by(State.id, State.name).first()
    if not first_state:
        print("Nothing")
    else:
        print("{}: {}".format(first_state.id, first_state.name))
    Session.close()
