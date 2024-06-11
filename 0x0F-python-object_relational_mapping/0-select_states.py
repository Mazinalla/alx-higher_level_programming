#!/usr/bin/env python3
'''
this is module for manibulating databases using MySQLdb and sqlalchemy
'''
import MySQLdb
import sys


def list_states(username, password, dbname):
    '''
    method that use for connect with database and make some queris
    '''
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

    # Execute the query to retrieve all states sorted by states.id
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

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

    # List all states
    list_states(username, password, dbname)
