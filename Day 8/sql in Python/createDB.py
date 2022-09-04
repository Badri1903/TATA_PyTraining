import sqlite3

conn = sqlite3.connect(database="employee.sqlite3")


conn.close()
