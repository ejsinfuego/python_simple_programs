
print("Record Keeping App")
print("a. Add Record")
print("b. View Records")
print("c. Clear All Records")
print("d. Exit")

user_input = input("Enter your choice: ")

while user_input != 'd':
    if user_input == "a":
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address: ")
        file = open("record.txt", "a")
        file.write(name + " " + email + " " + address + "\n")
        file.close()
        print("Record added.")
        user_input = input("Enter your choice: ")
    elif user_input == "b":
        file = open("record.txt", "r")
        print(file.read())
        file.close()
        user_input = input("Enter your choice: ")
    elif user_input == "c":
        file = open("record.txt", "w")
        file.write("")
        file.close()
        print("No records found.")
        user_input = input("Enter your choice: ")
    else:
        print("Invalid Input")
        user_input = input("Enter your choice: ")
else:
    print("Thank you")