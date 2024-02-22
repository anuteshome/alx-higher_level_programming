#!/usr/bin/python3
"""
This module contains a function called 'get_the_row_matches_given_name'
that takes four arguments mysql usrername, mysql password,
database name (hbtn_0e_0_usa), and name searched. And displays all
values in that rows.
"""
from sys import argv
import MySQLdb


def get_the_row_matches_given_name(username, password, db_name, searched):
    """Displays all values of a row in which name matches occur
        Args:
            username (str): mysql username
            password (str): mysql password
            db_name (str): database name
            searched (str): state name searched
    """
    db = MySQLdb.connect(
            host='localhost', user=username, passwd=password,
            db=db_name, port=3306)
    cur = db.cursor()
    query = "SELECT * FROM states WHERE binary name LIKE '{}'".format(searched)
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == '__main__':
    get_the_row_matches_given_name(argv[1], argv[2], argv[3], argv[4])
