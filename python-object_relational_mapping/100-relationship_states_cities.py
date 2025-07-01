#!/usr/bin/python3
"""
Script that creates the State "California" with the City "San Francisco"
from the database hbtn_0e_100_usa using ORM relationships.
"""

import sys
from relationship_state import Base, State
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

    # Create all tables
    Base.metadata.create_all(engine)

    # Create session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Create California state
        california = State(name="California")

        # Create San Francisco city
        san_francisco = City(name="San Francisco")

        # Method 1: Link using relationship attribute
        california.cities.append(san_francisco)

        # Alternative Method 2: Link using foreign key
        # san_francisco.state = california

        # Add to session and commit
        session.add(california)  # This also adds san_francisco automatically
        session.commit()

    except Exception as e:
        session.rollback()
        print(f"Error: {e}")

    finally:
        session.close()
