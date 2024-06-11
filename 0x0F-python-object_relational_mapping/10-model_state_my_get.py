#!/usr/bin/python3
"""
Script that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa.

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: MySQL database name
    state_name: State name to search

The script connects to a MySQL server running on localhost at port 3306,
and retrieves the State object with the given state name.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def print_state_by_name(username, password, dbname, state_name):
    # Create an engine that stores data in the local directory's hbtn_0e_6_usa database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State object with the given state name
    state = session.query(State).filter(State.name == state_name).first()

    # Print the state id or "Not found" if not found
    if state:
        print(state.id)
    else:
        print("Not found")

    # Close the session
    session.close()

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    state_name = sys.argv[4]

    # Print the state id by name
    print_state_by_name(username, password, dbname, state_name)
