# EXERCISE - PHONE BOOK
phone_book = {'badri':6379117697, 'avinash':7904094850, 'gayathri':9384418906, 'ashwin':9789671827, 'ammu':7448668533}
cont = 'y'
while cont=='y' or cont =='Y':
    name = input('Enter contact name: ')
    temp_name = name.lower()
    if temp_name in phone_book:
        print('Contact name:', name, '\nContact number:', phone_book[temp_name])
    else:
        print('Contact not found')
    cont = input('\nEnter y to continue or anything to exit: ')
    if cont != 'y' and cont != 'Y':
        break