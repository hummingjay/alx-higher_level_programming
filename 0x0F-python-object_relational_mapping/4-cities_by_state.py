#!/usr/bin/python3
"""
Script that prints all cities
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(port=3306, host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT states, cities FROM cities ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
