#!/usr/bin/python3
"""
Script that takes in arguments and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument. But this time,
write one that is safe from MySQL injections!
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
    check = (sys.argv[4], )
    cur.execute("SELECT * FROM states WHERE name = %s\
    ORDER BY states.id ASC", check)
    lst = cur.fetchall()
    for r in lst:
        print(r)
    cur.close()
    db.close()
