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
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=dbname,
        port=3306
    )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name = {} ORDER BY id ASC".format(state_name))

    states = cursor.fetchall()
    for state in states:
        print(state)

    cursor.close()
    db.close()

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]
    find_state(username, password, dbname, state_name)
