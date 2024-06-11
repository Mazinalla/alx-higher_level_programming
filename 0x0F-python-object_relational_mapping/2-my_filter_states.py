#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: MySQL database name
    state_name_searched: State name to search for

The script connects to a MySQL server running on localhost at port 3306,
and retrieves states whose name matches the provided argument, sorted by states.id in ascending order.
"""

import MySQLdb
import sys

def find_state(username, password, dbname, state_name):
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

    # Execute the query to retrieve states where name matches the argument
    cursor.execute(f"SELECT * FROM states WHERE name = {state_name} ORDER BY id ASC")

    # Fetch all the rows
    states = cursor.fetchall()

    # Print each state
    for state in states:
        print(state)

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Find and display states with the given name
    find_state(username, password, dbname, state_name)
