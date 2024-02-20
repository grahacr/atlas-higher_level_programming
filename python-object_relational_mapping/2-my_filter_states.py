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
    cursor.execute(
        """SELECT id, name FROM states
        WHERE LOWER(name) LIKE LOWER('{}')
        ORDER BY states.id ASC;""".format(state + "%")
    )
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
