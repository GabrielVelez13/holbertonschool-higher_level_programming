#!/usr/bin/python3
""" Looks for a state and prints its id. """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State

if __name__ == "__main__":
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

    """ Look for state. """
    for states in session.query(State).order_by(State.id).all():
        if sys.argv[4] == states.name:
            print(states.id)

    """ Close session. """
    session.close()
