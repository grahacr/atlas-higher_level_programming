#!/usr/bin/python3
"""
list cities and states utilizing join sql statement
"""


import sys
import MySQLdb

if __name__ == "__main__":
    connection = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )
    cursor = connection.cursor()
    cursor.execute(
        """SELECT cities.id, cities.name, states.name
    FROM cities JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC;"""
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conection.close()
