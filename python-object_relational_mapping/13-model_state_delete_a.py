#!/usr/bin/python3
""" Adds a new state. """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ Receiving information. """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Create engine. """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)

    """ Start session. """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Adding new state"""
    for states in session.query(State).order_by(State.id).all():
        if 'a' in states.name:
            session.delete(states)
    session.commit()

    """ Close session. """
    session.close()
