dict = {}
quit = False

def del_dict(dict):
    keyDelete = str(input('Enter the key to delete: '))
    del dict[keyDelete]
    print("Dictionary deleted!")
    if len(dict) >= 1:
        view_dict(dict)
    else:
        print("No current keys")
    
def add_dict(dict):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict.update({key:value})
    print("Student added!")
    print()

def view_dict(dict):
    for name in dict:
        print("key: ", name)
        print("value: ", dict[name])
    if len(dict) >= 1:
        view_dict(dict)
    else:
        print("No current keys")
    
while not quit:
    print("a - Add data")
    print("d - Delete data")
    print("v - View data")
    print("q - Quit")
    choice = str(input("Enter your choice: "))

    if choice == "a":
        add_dict(dict)
    elif choice == "d":
        del_dict(dict)
    elif choice == "v":
        view_dict(dict)
    elif choice == "q":
        quit = True
        print("Thank you.")
    else:
        print("Invalid choice!")
    print()
    

