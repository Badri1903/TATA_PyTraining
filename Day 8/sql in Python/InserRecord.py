import sqlite3

conn = sqlite3.connect(database="employee.sqlite3")

cursor = conn.cursor()

# qry = "insert into emp values ('emp-001', 'Mike Tyson', 'boxing', 'boxer', 95000)"
# qry = "insert into emp values ('emp-002', 'Roger Fedrer', 'Tennis', 'tennis player', 80000)"
# qry = "insert into emp values ('emp-003', 'Sachin Tendulkar', 'Cricket', 'batsman', 98000)"
# qry = "insert into emp values ('emp-004', 'PV Sindhu', 'Badmiton', 'badmiton', 75000)"
qry = "insert into emp values ('emp-005', 'Carl Lewis', 'Running', '100 mts', 90000)"

cursor.execute(qry)

conn.commit()
conn.close()
