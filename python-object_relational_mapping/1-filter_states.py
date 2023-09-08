#!/usr/bin/python3
"""
Script to list all states with a name starting with 'N'
should take 3 arguments username, passwd and db name
"""


if __name__ == "__main__":
    import sys
    import MySQLdb
    mysql_user = sys.argv[1]
    mysql_passwd = sys.argv[2]
    mysql_db = sys.argv[3]
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_user,
                         passwd=mysql_passwd, db=mysql_db)
    curr = db.cursor()
    curr.execute("SELECT * FROM states where name LIKE 'N%'\
                 ORDER BY states.id ASC")
    query_rows = curr.fetchall()
    for row in query_rows:
        if row[1][0] == 'N':
            print(row)
    curr.close()
    db.close()
