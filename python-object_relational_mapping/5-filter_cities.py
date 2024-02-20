#!/usr/bin/python3
"""
list cities associated with given state name
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
    state = sys.argv[4]
    cursor.execute(
        """SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id
        WHERE LOWER(states.name) LIKE LOWER(%s)
        ORDER BY cities.id ASC;""",
        (state + '%',)
    )
    cities = cursor.fetchall()
    city_names = ', '.join(city[0] for city in cities)
    print(city_names)
    cursor.close()
    connection.close()
