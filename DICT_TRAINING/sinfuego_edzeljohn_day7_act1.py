import random

print("Name Generator")

firstname = ['maria', 'pedro', 'mila', 'juan', 'petra', 'mario', 'jose', 'andres', 'sikent', 'sheri']

middlename = ['cruz', 'pilar', 'smith', 'perez', 'sante', 'sinag', 'vicente', 'marcos', 'pintal', 'sonit']

lastname = ['deloSantos', 'manti', 'purkil', 'mikra', 'shotki','mintra','skita','kufti', 'minta','joic']

names = []
user = str(input('Enter yes to generate a name: '))

def generateName(firstname, middlename, lastname):
    firstname = str(firstname[random.randrange(0,9)])
    middlename = str(middlename[random.randrange(0,9)])
    lastname = str(lastname[random.randrange(0,9)])
    completeName = firstname + " " + middlename +" "+ lastname
    names.append(completeName)
    return print("Congratulations! Your new name is", completeName.title())

while user == 'yes':
    generateName(firstname, middlename, lastname)
    user = str(input('Would you like to generate a new name: \n'))
else:
    print('Thank you for using the name generator')
    print('Here are the names you generated')
    for i in names:
        print("--",str.title(i))
    