#!/usr/bin/python3
"""lists all states from the database hbtn_0e_0_usa """
import sys
import MySQLdb


# program entry
if __name__ == "__main__":
    if len(sys.argv) < 5:
        """ this checks if the args are less than required"""
        print("Usage: python3 script.py username password
              database name")
        sys.exit(1)

    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)

    namearg = sys.argv[4]

    cur = db.cursor()

    cur.execute("SELECT * FROM states WHERE name LIKE '{}'
                ORDER BY id ASC".format(namearg))

    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    db.close()
