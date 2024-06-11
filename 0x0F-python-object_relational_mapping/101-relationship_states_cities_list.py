#!/usr/bin/python3
"""
Script that lists all State objects, and corresponding City objects,
contained in the database hbtn_0e_101_usa.

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: MySQL database name

The script connects to a MySQL server running on localhost at port 3306,
and lists all State objects along with their corresponding City objects,
sorted in ascending order by states.id and cities.id.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

def list_states_and_cities(username, password, dbname):
    # Create an engine that stores data in the local directory's hbtn_0e_101_usa database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all State objects and their associated City objects, sorted by states.id and cities.id
    states = session.query(State).order_by(State.id, City.id).all()

    # Print the states and their cities
    for state in states:
        print(f"{state.name}:")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")
    
    # Close the session
    session.close()

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # List all State objects and their corresponding City objects
    list_states_and_cities(username, password, dbname)
