#!/usr/bin/python3
"""
Script that takes the name of a state as an argument and lists all cities
of that state, using the database hbtn_0e_4_usa.
Safe from MySQL injections!
"""

import MySQLdb
import sys


def main():
    """
    Main function that connects to MySQL and lists cities by state name.
    Uses parameterized queries to prevent SQL injection attacks.
    """

    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create cursor
    cursor = db.cursor()

    # SAFE WAY: Use parameterized query with %s placeholder
    # The %s is NOT Python string formatting - it's MySQL parameter binding
    query = (
        "SELECT cities.name "
        "FROM states "
        "JOIN cities ON states.id = cities.state_id "
        "WHERE BINARY states.name = %s "
        "ORDER BY cities.id ASC"
    )

    # Execute with parameters - to avoid SQL injection
    cursor.execute(query, (state_name,))  # execute once only

    # Fetch and display results
    results = cursor.fetchall()

    # format the result, join city names  with commas
    if results:
        print(", ".join([row[0] for row in results]))
    else:
        print()  # print empty line if no result found

    # Clean up
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
