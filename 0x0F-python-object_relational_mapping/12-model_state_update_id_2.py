#!/usr/bin/python3
"""
Script that changes the name of a State object from the database hbtn_0e_6_usa.

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: MySQL database name

The script connects to a MySQL server running on localhost at port 3306,
and changes the name of the State object where id = 2 to "New Mexico".
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
import sys

def update_state_name(username, password, dbname):
    # Create an engine that stores data in the local directory's hbtn_0e_6_usa database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query the State object with id = 2
    state = session.query(State).filter_by(id=2).first()

    # Update the name of the state if found
    if state:
        state.name = "New Mexico"
        session.commit()
        print("Name updated successfully")
    else:
        print("State with id=2 not found")

    # Close the session
    session.close()

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Update the name of the State object with id=2
    update_state_name(username, password, dbname)
