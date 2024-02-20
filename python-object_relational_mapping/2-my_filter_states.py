#!/usr/bin/python3
"""
display values of states table associated with argument
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
    query = "SELECT id, name FROM states WHERE name LIKE '{}' ORDER BY states.id ASC".format(state + "%")
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()