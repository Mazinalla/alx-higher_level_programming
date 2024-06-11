#!/usr/bin/python3
"""
Script that lists all states with a name starting with 'N' from the database hbtn_0e_0_usa.

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: MySQL database name

The script connects to a MySQL server running on localhost at port 3306,
and retrieves states whose names start with 'N', sorted by states.id in ascending order.
"""
import MySQLdb
import sys



def list_states_with_n(username, password, dbname):
    '''
    function that get arguments from user to connect to database and make queris
    '''
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=dbname,
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE LOWER(name) LIKE 'N%' ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    list_states_with_n(username, password, dbname)
