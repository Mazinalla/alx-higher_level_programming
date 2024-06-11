#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa. This script is safe from SQL injections.

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: MySQL database name
    state_name: State name

The script connects to a MySQL server running on localhost at port 3306,
and retrieves all cities of the specified state, sorted by cities.id in ascending order.
"""

import MySQLdb
import sys

def list_cities_by_state(username, password, dbname, state_name):
    # Connect to the database
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=dbname,
        port=3306
    )

    # Create a cursor object
    cursor = db.cursor()

    # Execute the query to retrieve cities for the given state name
    query = """
    SELECT cities.id, cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows
    cities = cursor.fetchall()

    # Print the cities
    city_names = [city[1] for city in cities]
    print(", ".join(city_names))

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # List all cities for the given state name
    list_cities_by_state(username, password, dbname, state_name)
