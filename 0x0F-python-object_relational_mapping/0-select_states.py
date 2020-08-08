#!/usr/bin/python3
''' script that lists all states from the database hbtn_0e_0_usa '''


import MySQLdb
import sys


if __name__ == "__main__":
    sql_usr = sys.argv[1]
    sql_pass = sys.argv[2]
    data = sys.argv[3]
    db = MySQLdb.connect(user=sql_usr, passwd=sql_pass, db=data)
    cursor = db.cursor()
    query = 'SELECT * FROM states ORDER BY states.id;'
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
