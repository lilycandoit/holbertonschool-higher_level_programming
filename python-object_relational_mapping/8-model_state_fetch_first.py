#!/usr/bin/python3
"""
Script that prints the first State object from the database hbtn_0e_6_usa.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    # Create database connection
    database_url = (
        f"mysql+mysqldb://{mysql_username}:{mysql_password}"
        f"@localhost:3306/{database_name}"
        )

    engine = create_engine(database_url, pool_pre_ping=True)

    # Create a session (this is like a cursor in raw SQL)
    Session = sessionmaker(bind=engine)
    session = Session()

    # Get the first state (ordered by states.id which is default)
    # .first() returns the first result or None if no results
    first_state = session.query(State).order_by(State.id).first()

    # Display results in the required format
    if first_state:
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")

    # Close session
    session.close()
