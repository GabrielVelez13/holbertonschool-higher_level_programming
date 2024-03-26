#!/usr/bin/python3
""" Print the first state. """

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """ Doesn't run on import. """
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{username}:{password}@localhost:3306/{database}"
    )

    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    firstState = session.query(State).order_by(State.id).first()
    print(f"{firstState.id}: {firstState.name}")

    session.close()
