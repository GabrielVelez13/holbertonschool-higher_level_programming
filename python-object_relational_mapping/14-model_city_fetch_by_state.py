#!/usr/bin/python3
""" Prints all cities. """


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from model_state import Base, State
from model_city import City

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

    state = (session.query(State, City)
             .filter(City.state_id == State.id).order_by(State.id))

    for states, cities in state:
        print(f"{states.name}: ({cities.id}) {cities.name}")

    session.close()
