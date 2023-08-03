myList = []

ask = input('Add a word to the list: ')
add = 'y'
while ask.isalpha() and add == 'y':
    myList.append(ask)
    add = input('Add another word to the list (y/n): ')
    if add == 'y':
        ask = input('Add a word to the list: ')
    else:
        print('Words in list are ', len(myList), ' and they are: ')
        for i in range(len(myList)):
            print('--',myList[i])
        print('\nThankyou!')
        break




    