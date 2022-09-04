#                                  .....::::: JSON :::::....

import json
from prettytable import PrettyTable

JFR = open('books.json', 'r')
json_file = json.load(JFR)        #      json in Python  ---> python

for book in json_file['books']:
    print(book['name'].upper())
    print("-"*20)
    for k,v in book.items():
        print(k, '=>', v)
    print('=' * 30,'\n')

print('=*' * 40)

for book in json_file['books']:
    bookTbl = PrettyTable(book.keys())

for book in json_file['books']:
    bookTbl.add_row(book.values())

bookTbl.align['name'] = 'l'
print(bookTbl)

