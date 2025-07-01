#!/usr/bin/python3
"""
Script that safely filters states using parameterized queries.
Safe from MySQL injections!
"""

import MySQLdb
import sys


def main():
    """
    Main function that safely connects to MySQL and filters states.
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
    query = "SELECT * FROM states WHERE BINARY name = %s ORDER BY id ASC"

    # Execute with parameters - MySQL handles escaping automatically
    cursor.execute(query, (state_name,))  # to avoid SQL injection

    # Fetch and display results
    results = cursor.fetchall()
    for row in results:
        print(row)

    # Clean up
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
