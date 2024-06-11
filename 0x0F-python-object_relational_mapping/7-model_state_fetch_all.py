#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: MySQL database name

The script connects to a MySQL server running on localhost at port 3306,
and retrieves all State objects sorted by states.id in ascending order.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def list_states(username, password, dbname):
    # Create an engine that stores data in the local directory's hbtn_0e_6_usa database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}', echo=True)

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects and sort by id
    states = session.query(State).order_by(State.id).all()

    # Print the states
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # List all states
    list_states(username, password, dbname)
