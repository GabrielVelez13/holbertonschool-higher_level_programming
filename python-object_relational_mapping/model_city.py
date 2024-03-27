#!/usr/bin/python3
""" Creating a new class that creates a relationship between two classes. """

from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """ Defining the class City. """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("State.id"), nullable=False)
