#!/usr/bin/python3
"""
Script that  lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb
import sys


def main():
    """
    Lists all cities from the database hbtn_0e_4_usa
    Return: results sorted in ascending order by cities.id
    """

    # Get command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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

    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM states "
        "JOIN cities ON states.id = cities.state_id "
        "ORDER BY cities.id ASC"
        )

    # Execute with parameters - MySQL handles escaping automatically
    cursor.execute(query)  # to avoid SQL injection

    # Fetch and display results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Clean up
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
