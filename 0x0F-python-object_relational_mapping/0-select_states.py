#!/usr/bin/python3
"""
This module contains a function called 'get_all_states'
that takes three arguments mysql usrername, mysql password, and
database name (hbtn_0e_0_usa) and lists all rows in states table.
"""
import MySQLdb
import sys


def get_all_states(username, password, db_name):
    """Lists rows in the states table from the database `hbtn_0e_usa`
        Args:
            username (str): mysql username
            password (str): mysql password
            db_name (str): database name
    """
    db = MySQLdb.connect(
            host='localhost', user=username, passwd=password,
            db=db_name, port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    get_all_states(sys.argv[1], sys.argv[2], sys.argv[3])
