#!/usr/bin/python3
"""
Contains the class definition of a State and an instance
Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create the Base instance that all models will inherit from
Base = declarative_base()


class State(Base):
    """
    State class that represents the states table in MySQL database.

    Attributes:
        id (int): Auto-generated unique integer, primary key
        name (str): State name, max 128 characters, cannot be null
    """

    # Tell SQLAlchemy which table this class maps to
    __tablename__ = 'states'

    # Define the columns
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    # Define the relationship to cities (one-to-many)
    cities = relationship(
        "City", back_populates="state", cascade="all, delete-orphan")
