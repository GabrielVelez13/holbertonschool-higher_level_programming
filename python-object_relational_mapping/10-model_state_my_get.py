#!/usr/bin/python3
""" Looks for a state and prints its id. """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    """ Receiving information. """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    StateName = sys.argv[4]

    """ Create engine. """
    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)

    """ Start session. """
    Session = sessionmaker(bind=engine)
    session = Session()

    """ Look for state. """
    state = session.query(State).filter_by(name=StateName).first()
    if state:
        print(state.id)
    else:
        print("Not found")

    """ Close session. """
    session.close()
