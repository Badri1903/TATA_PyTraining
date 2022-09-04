# checking keys

sample_dic = {1:10, 2:20, 3:30, 4:40, 5:50, 6:60}
print('Given dictionary:', sample_dic, '\n')

cont = 'y'
while cont == 'y':
    try:
        k = int(input('Enter a key: '))
        if k in sample_dic:
            print('This key already exists!')
        else:
            print('Warning: It\'s a new key!')
    except:
        print('Key should be an integer')
    cont = input("Enter \'y\' to try again or anything to exit: ")
