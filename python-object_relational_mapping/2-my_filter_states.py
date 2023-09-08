#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
takes 4 arguments username, passwd, db name and state name searched
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
    cur.execute("SELECT * FROM states WHERE name = '{}'\
    ORDER BY states.id ASC".format(sys.argv[4]))
    lst = cur.fetchall()
    for r in lst:
        if r[1] == sys.argv[4]:
            print(r)
    cur.close()
    db.close()
