#!/usr/bin/python3
'''
this is module for manibulating databases using MySQLdb and sqlalchemy
'''
import MySQLdb
import sys


def list_states(username, password, dbname):
    '''
    method that use for connect with database and make some queris
    '''
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=dbname,
        port=3306
    )
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    states = cursor.fetchall()
    for state in states:
        print(state)
    cursor.close()
    db.close()
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    list_states(username, password, dbname)


