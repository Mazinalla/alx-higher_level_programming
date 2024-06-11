#!/usr/bin/python3
"""
Script that creates the State “California” with the City “San Francisco” 
from the database hbtn_0e_100_usa.

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: MySQL database name

The script connects to a MySQL server running on localhost at port 3306,
and creates the State "California" with the City "San Francisco" from the specified database.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City
import sys

def create_state_city(username, password, dbname):
    # Create an engine that stores data in the local directory's hbtn_0e_100_usa database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Create a State object for "California"
    california = State(name="California")

    # Create a City object for "San Francisco"
    san_francisco = City(name="San Francisco")

    # Add the city to the state
    california.cities.append(san_francisco)

    # Add the state and city to the session
    session.add(california)
    session.commit()

    # Close the session
    session.close()

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Create the State "California" with the City "San Francisco"
    create_state_city(username, password, dbname)
