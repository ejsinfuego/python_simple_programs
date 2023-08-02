quit = str(input("Do you want to quit? (y/n): "))

while quit == "n":
    office = str(input("Enter your office: "))
    offices = ['it', 'human resource', 'accounting']
    if office.lower() != 'it' or 'human resource' or 'accounting':
        years = int(input("Enter your years of service: "))
        print("Office: ", office.capitalize())
        if office.lower() == 'it':
            if years >= 10:
                print("Your bonus is 10000")
            else:
                print("Your bonus is 5000")
        elif office.lower() == 'human resource':
            if years >= 10:
                print("Your bonus is 12000")
            else:
                print("Your bonus is 6000")
        elif office.lower() == 'accounting':
            if years >= 10:
                print("Your bonus is 15000")
            else:
                print("Your bonus is 7500")
    else:
        print("Office not found, Try again.")
        office = str(input("Enter your office: "))
    finally_quit = str(input("Do you want to quit? (y/n): "))
else:
    print('bye')
                
    