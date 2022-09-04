import csv
from prettytable import PrettyTable

with open('Employee.csv', 'r') as CSVR:
    emp_details = csv.reader(CSVR)
    #colname = next(CSVR)
    #print(colname)
    emp_tabl = PrettyTable(next(emp_details))

    #for rec in emp_details:
        #print(rec)

    for rec in emp_details:
        emp_tabl.add_row(rec)

print(emp_tabl)
