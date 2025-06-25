#!/usr/bin/python3
"""
Script that lists all states with a name starting with N from the database.
"""

# Import required modules
import MySQLdb
import sys   # For command line arguments


def main():
    """Connects to MySQL and lists all states that start with 'N' """
    # get input from command lines
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # connect MySQL database
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database,
    )

    # create a cursor object to execute SQL queries and fetch results
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    # fetch all rows
    results = cursor.fetchall()

    for row in results:
        print(row)

    # close cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
