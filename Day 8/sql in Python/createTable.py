import sqlite3

conn = sqlite3.connect("employee.sqlite3")

cursor = conn.cursor()

qry = ("""create table emp  (
     empid varchar(7) Primary Key,
     empname varchar(50) Not Null,
     dept varchar(25) Not Null,
     desig varchar(25) Not Null,
     salary double(7,2) Not Null)
      """)

cursor.execute(qry)

conn.close()
