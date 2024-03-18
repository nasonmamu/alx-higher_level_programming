#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa."""

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
    query = "SELECT cities.id, cities.name, states.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             ORDER BY cities.id ASC"
    cursor.execute(query)

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Print the rows
    for row in rows:
        print(row)

    # Close cursor and database connection
    cursor.close()
    db.close()
