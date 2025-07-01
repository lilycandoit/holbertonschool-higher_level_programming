#!/usr/bin/python3
"""
Script that deletes all State objects with a name
containing the letter a from the database
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

    # find state containing 'a'
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
        ).all()

    # update it if found
    if states_to_delete:
        for state in states_to_delete:
            session.delete(state)
        session.commit()  # commit to save the changes

    # Close session
    session.close()
