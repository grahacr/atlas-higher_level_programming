#!/usr/bin/python3
"""
module to utilize sqlalchemy to list all states in database
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
    """retrieve all data for use"""
    Base.metadata.create_all(engine)
    """use bind method to bind engine to session"""
    Session = sessionmaker(bind=engine)
    """create session instance"""
    session = Session()
    """query the results and print states"""
    for instance in session.query(State).order_by(State.id).all():
        print("{}: {}".format(instance.id, instane.name))
    Session.close()
