import sqlite3
from prettytable import from_db_cursor

conn = sqlite3.connect(database="employee.sqlite3")

cursor = conn.cursor()

qyr = "select * from emp"

cursor.execute(qyr)

empTbl = from_db_cursor(cursor)

print(empTbl)