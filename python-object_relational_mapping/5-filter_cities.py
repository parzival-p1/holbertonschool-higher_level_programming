#!/usr/bin/python3
"""
Script that takes in the name of a state as an argument and lists all cities of
that state, using the database hbtn_0e_4_usa
Script should take 4 arguments: mysql username, mysql password, database name
and state name (SQL injection free!)
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
    cur.execute("SELECT * FROM cities JOIN states\
    ON cities.state_id = states.id WHERE states.name = %s\
    ORDER BY cities.id ASC", check)
    lst = cur.fetchall()
    cities = []
    for r in lst:
        if r[4] == check[0]:
            cities.append(r[2])
    print(', '.join(cities))
    cur.close()
    db.close()
