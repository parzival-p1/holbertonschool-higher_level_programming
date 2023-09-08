#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa.
Script should take 3 arguments: mysql username, mysql password and database
name.
"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                         passwd=mysql_passwd, db=mysql_db)
    cur = db.cursor()
    cur.execute("SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id ORDER BY cities.id ASC")
    lst = cur.fetchall()
    for r in lst:
        print(r)
    cur.close()
    db.close()
