#!/usr/bin/python3
"""
Script that prints the State object with the name
passed as argument
from the database hbtn_0e_6_usa.

Safe from MySQL injections!
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
    state_search = sys.argv[4]

    # Create database connection
    database_url = (
        f"mysql+mysqldb://{mysql_username}:{mysql_password}"
        f"@localhost:3306/{database_name}"
    )
    engine = create_engine(database_url, pool_pre_ping=True)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Find state by name (safe from SQL injection)
    # Using .filter() with exact match
    state = session.query(State).filter(
        State.name == state_search
    ).first()

    if state:
        print(state.id)
    else:
        print("Not found")

    # Close session
    session.close()
