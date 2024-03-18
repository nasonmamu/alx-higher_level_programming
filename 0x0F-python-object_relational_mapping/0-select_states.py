#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute SQL query
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()

