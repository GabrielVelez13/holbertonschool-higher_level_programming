#!/usr/bin/python3
""" List all states from a data base. """

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Creating the engine. """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )
    Base.metadata.create_all(engine)

    """ Making the session. """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Finding the data. """
    for states in session.query(State).all():
        print(f"{states.id}: {states.name}")

    """ Closing the session. """
    session.close()
