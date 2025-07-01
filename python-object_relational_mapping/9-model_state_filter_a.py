#!/usr/bin/python3
"""
List all State objects containing the letter 'a' from the database
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

    # Filter states with 'a'
    filtered_states = session.query(State)\
        .filter(State.name.like('%a%'))\
        .order_by(State.id)\
        .all()

    # Display results in the required format
    for state in filtered_states:
        print(f"{state.id}: {state.name}")

    # Close session
    session.close()
