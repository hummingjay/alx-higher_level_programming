#!/usr/bin/python3
"""
script that takes arg and displays values from states table
where name matches arg, write it safe MySQL injections
"""
import MySQLdb
import sys

if __name__ = "__main__":
    # connect to db
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # initialize cursor
    cur = db.cursor()
    # initialize to avoid injection
    query = "SELECT * FROM states WHERE name = %s"
    namearg = sys.argv[4]
    # execute
    cur.execute(query, (namearg,))
    # fetch rows
    rows = cur.fetchall()
    # printing
    for row in rows:
        print(row)
    # close cursor
    cur.close()
    # close database
    db.close()
