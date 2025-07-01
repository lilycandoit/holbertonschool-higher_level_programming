#!/usr/bin/python3
"""
Script that changes the name of a State object from the database
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

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # find state with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    # update it if found
    if state_to_update:
        state_to_update.name = "New Mexico"
        session.commit()  # commit to save the changes

    # Close session
    session.close()
