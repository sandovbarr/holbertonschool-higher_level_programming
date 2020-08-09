#!/usr/bin/python3
''' script that lists all states from the database hbtn_0e_0_usa '''


import MySQLdb
import sys


if __name__ == "__main__":
    sql_usr = sys.argv[1]
    sql_pass = sys.argv[2]
    data = sys.argv[3]
    state = sys.argv[4]
    db = MySQLdb.connect(user=sql_usr, passwd=sql_pass, db=data)
    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities\
            INNER JOIN states ON cities.state_id = states.id\
            WHERE states.name = %s\
            ORDER BY cities.id", (state, ))
    query_rows = cursor.fetchall()
    for row in range(len(query_rows)):
        if row == len(query_rows) - 1:
            print(query_rows[row][0])
        else:
            print(query_rows[row][0], end=", ")
    cursor.close()
    db.close()
