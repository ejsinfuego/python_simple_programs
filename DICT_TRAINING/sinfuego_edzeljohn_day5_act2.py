def string_reverser():
    string = input('Enter a string: ')
    print('INPUT:',string)
    print('OUTPUT:',string.upper()[::-1], '(',len(string),') Characters')

string_reverser()