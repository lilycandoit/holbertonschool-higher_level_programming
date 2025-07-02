#!/usr/bin/python3
"""
Contains the class definition of a City and an instance
Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from relationship_state import Base
from sqlalchemy.orm import relationship


class City(Base):
    """
    City class that represents the cities table in MySQL database.

    Attributes:
        id (int): Auto-generated unique integer, primary key
        name (str): City name, max 128 characters, cannot be null
        state_id (int): Foreign key to states table, cannot be null
    """

    # Tell SQLAlchemy which table this class maps to
    __tablename__ = 'cities'

    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    name = Column(String(128), nullable=False)

