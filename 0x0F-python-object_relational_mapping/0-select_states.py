#!/usr/bin/python3
'''
This is a python script that lists all states from
the database hbtn_0e_0_usa.
'''
import MySQLdb

# connecting to a MySQL database
db = MySQLdb.connect(host="localhost", user=username,
                     passwd=password, db=database, port=3306)

# creating cursor
cur = db.cursor()

# script to execute listing of states
cur.execute("SELECT * FROM states ORDER BY id ASC")

# fetching all at once
rows = cur.fetchall()

# print out data
for row in rows:
    print(row)

# close the open cursor
cur.close()

# close open database
db.close()

# program entry point to avoid running if imported
if __name__ == "__main__":
    import sys

    # retrieve command line inputs
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    # call the function to list states
    list_states(username, password, database)
