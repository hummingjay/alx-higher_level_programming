#!/usr/bin/python3
'''
script that takes in an argument and displays all values in
the states table of hbtn_0e_0_usa where name matches arg
'''
import sys
import MySQLdb

if __name__ == "__main":
    db = MySQLdb.connect(host="localhost", user=argv[1],
                         passwd=argv[2], db=argv[3], port=3306)

    namearg = argv[4]

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE
                   '{namearg}' ORDER BY id ASC")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
