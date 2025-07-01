#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa
"""

import sys
from relationship_state import State
from relationship_city import City
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

    try:
        states = session.query(State).order_by(State.id).all()

        for state in states:
            print(f"{state.id}: {state.name}")

            # Cities are already loaded, sort them by id
            cities = sorted(state.cities, key=lambda city: city.id)

            for city in cities:
                print(f"\t{city.id}: {city.name}")

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()
