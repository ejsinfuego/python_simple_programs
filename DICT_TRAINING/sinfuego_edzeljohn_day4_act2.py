quit = 'y'
ask = 'Would you like to try again (y/n): '
while quit != 'n':
    num = input("\nEnter a number: ")
    while num.isdigit() == False and num != 'q':
        print("Please enter a valid number or q to quit")
        num = input("Enter a number: ")
    if num == 'q':
        break
    else:
        num = int(num)
    num2 = input("Enter another number: ")
    if num2.isdigit() == False and num2 != 'q':
        print("Please enter a valid number. or q to quit")
        num2 = input("Enter a number: ")
    if num == 'q':
        break
    else:
        num2 = int(num2)
    print('The sum of the two numbers is: ', num + num2)
    print('====================================')
    quit = input(ask)
print('====================================')
print("Thank you!")

