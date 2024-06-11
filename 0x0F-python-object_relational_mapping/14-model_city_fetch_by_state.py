#!/usr/bin/python3
"""
Script that prints all City objects from the database hbtn_0e_14_usa.

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: MySQL database name

The script connects to a MySQL server running on localhost at port 3306,
and prints all City objects from the specified database, sorted by cities.id.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City
import sys

def fetch_cities_by_state(username, password, dbname):
    # Create an engine that stores data in the local directory's hbtn_0e_14_usa database
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost:3306/{dbname}')

    # Bind the engine to the metadata of the Base class
    Base.metadata.bind = engine

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session
    session = Session()

    # Query all City objects and sort by cities.id
    cities = session.query(City).order_by(City.id).all()

    # Print the cities
    for city in cities:
        print(f"{session.query(State).filter(State.id == city.state_id).first().name}: ({city.id}) {city.name}")

    # Close the session
    session.close()

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # Print all City objects from the specified database
    fetch_cities_by_state(username, password, dbname)