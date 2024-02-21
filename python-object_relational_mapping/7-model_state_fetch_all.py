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

    engine = create_engine(
        'mysql://{}:{}@localhost/{}'.format(username, password, db)
        )
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State).order_by(State.id).all():
        print("{}: {}".format(instance.id, instane.name))
    Session.close()
