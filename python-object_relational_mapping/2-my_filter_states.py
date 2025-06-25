#!/usr/bin/python3
"""
Script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
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
    keyword = sys.argv[4]

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

    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC"
    cursor.execute(query.format(keyword))

    # fetch all rows
    results = cursor.fetchall()

    for row in results:
        print(row)

    # close cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
