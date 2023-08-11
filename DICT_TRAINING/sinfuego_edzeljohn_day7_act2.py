# 1. Create a calculator app
# 2. The user will choose between the 4 math operations (Add, Subtract, Multiply and Divide)
# 3. The application will ask for 2 numbers
# 4. Display the result
# 5. The application will ask again if the user wants to try again
# 6. Use the appropriate Exception (ex: Invalid input such as text and zero division)


def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2


def calculator():
    print("Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Quit")
    print()
    choice = int(input("Enter your choice: "))
    while choice != 5:
        if choice == 1:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                print("Result: ", add(num1, num2))
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input!")
                choice = int(input("Enter your choice: "))
        elif choice == 2:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                print("Result: ", subtract(num1, num2))
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input!")
                choice = int(input("Enter your choice: "))
        elif choice == 3:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                print("Result: ", multiply(num1, num2))
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input!")
                choice = int(input("Enter your choice: "))
        elif choice == 4:
            try:
                num1 = int(input("Enter first number: "))
                num2 = int(input("Enter second number: "))
                print("Result: ", divide(num1, num2))
                choice = int(input("Enter your choice: "))
            except ValueError:
                print("Invalid input!")
                choice = int(input("Enter your choice: "))
            except ZeroDivisionError:
                print("Cannot divide by zero!")
                choice = int(input("Enter your choice: "))
        else:
            print("Invalid choice!")
            choice = int(input("Enter your choice: "))
    else:
        print("Thank you.")
        
calculator()