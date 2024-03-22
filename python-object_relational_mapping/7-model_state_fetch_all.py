#!/usr/bin/python3
""" List all states from a data base. """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    """ Creating the engine. """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    """ Making the session. """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Finding the data. """
    for states in session.query(State).order_by(State.id):
        print(f"{states.id}: {states.name}")

    """ Closing the session. """
    session.close()
