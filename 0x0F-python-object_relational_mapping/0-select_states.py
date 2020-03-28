#!/usr/bin/python3
""" shebang line - defines where the interpreter is located """
""" script that lists all states from the database hbtn_0e_0_usa """
from sys import argv
""" module to receive arguments """
import MySQLdb
""" module to connect to a MySQL database and execute SQL statements """
if __name__ == "__main__":
    """ execute only if run as a sript """
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        charset="utf8"
    )
    cur = conn.cursor()
    try:
        stmt = """
        SELECT * FROM states;
        """
        cur.execute(stmt)
        rtn = cur.fetchall()
    except MySQLdb.Error:
        try:
            print ("MySQLdb Error")
        except IndexError:
            print ("MySQLdb Error - IndexError")
    for row in rtn:
        print(row)
    cur.close()
    """ Close all cursors """
    conn.close()
    """ Close all databases """
