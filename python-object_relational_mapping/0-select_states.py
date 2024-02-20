#!/usr/bin/python3
""" module to utilize python ORM to run simple sql query """


import MySQLdb
import sys

if __name__ == "__main__":
    connection = MySQLdb.connect(host="localhost", user="root", password="root", database="hbtn_0e_0_usa")
    cursor = connection.cursor()
    query = "SELECT id, name FROM states ORDER BY states.id ASC"
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    connection.close()
