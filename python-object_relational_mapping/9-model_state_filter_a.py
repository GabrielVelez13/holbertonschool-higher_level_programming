#!/usr/bin/python3
""" Listing all states in db that have an 'a' in its name. """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ Receiving information. """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Creating engine. """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)

    """ Creating session. """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Printing all states with a in its name. """
    for states in session.query(State).order_by(State.id).all():
        if 'a' in states.name:
            print(f"{states.id}: {states.name}")

    """ Closing session. """
    session.close()
