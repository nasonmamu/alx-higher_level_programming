#!/usr/bin/python3
"""Lists all cities of a given state from the database hbtn_0e_4_usa."""

import sys
import MySQLdb

if __name__ == "__main__":
    # Database connection parameters
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

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
    query = "SELECT cities.name FROM cities \
             JOIN states ON cities.state_id = states.id \
             WHERE states.name = %s ORDER BY cities.id ASC"
    cursor.execute(query, (state_name,))

    # Fetch all the rows in a list of tuples
    rows = cursor.fetchall()

    # Check if there are cities in the given state
    if rows:
        # Print the cities
        cities = ", ".join(row[0] for row in rows)
        print(cities)
    else:
        print()

    # Close cursor and database connection
    cursor.close()
    db.close()
