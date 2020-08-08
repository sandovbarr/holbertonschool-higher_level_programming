#!/usr/bin/env python3
''' script that lists all states from the database hbtn_0e_0_usa '''


import MySQLdb
import sys


if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    db = MySQLdb.connect(user=mysql_username,
                        passwd=mysql_password,
                        db=database_name)
    cursor = db.cursor()
    query = 'SELECT * FROM states ORDER BY states.id;'
    cursor.execute(query)
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)
    cursor.close()
    db.close()
