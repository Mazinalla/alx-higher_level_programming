#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.

Arguments:
    mysql_username: MySQL username
    mysql_password: MySQL password
    database_name: MySQL database name

The script connects to a MySQL server running on localhost at port 3306,
and retrieves all cities, sorted by cities.id in ascending order.
"""
import MySQLdb
import sys



def list_cities(username, password, dbname):
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

    # Execute the query to retrieve all cities sorted by id
    query = """
    SELECT cities.id, cities.name, states.name 
    FROM cities 
    JOIN states ON cities.state_id = states.id 
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Fetch all the rows
    cities = cursor.fetchall()

    # Print each city
    for city in cities:
        print(f"({city[0]}, '{city[1]}', '{city[2]}')")

    # Close the cursor and database connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]

    # List all cities
    list_cities(username, password, dbname)
