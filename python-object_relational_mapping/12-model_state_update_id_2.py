#!/usr/bin/python3
"""
module to update name of state object in database
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

    """create engine to connect to database"""
    engine = create_engine(
        f'mysql://{username}:{password}@localhost/{db}'
    )
    """collect data from engine"""
    Base.metadata.create_all(engine)
    """start session using bind"""
    Session = sessionmaker(bind=engine)
    """create new session instance"""
    session = Session()
    """query for state matching certain id"""
    state_update = session.query(State).filter(State.id == 2).first()
    if state_update:
        """update name of State"""
        state_update.name = 'New Mexico'
        """commit session to database"""
        session.commit()
    """close session"""
    session.close()
