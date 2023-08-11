
import reservation as reservation

print("Restaurant Reservation System")
print("-----------------------------")
print("\n1. Make Reservation")
print("2. View Reservations")
print("3. Delete Reservation")
print("4. Generate Report")
print("5. Quit")

def viewReservation():
    print("View Reservations")
    print("No.\tName\tDate\t\t Time\t  Children\tAdults\t")
    print("="*70)

    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()
            if lines:
                reservations = []
                reservation = {}
                for line in lines:
                    line = line.strip()
                    if line:    
                        key, value = line.split(": ")
                        reservation[key] = value
                    else:
                        reservations.append(reservation)
                        reservation = {}
                
                for idx, res in enumerate(reservations, start=1):
                    print(
                        idx,"\t", res["Name"], "\t", res["Date"], "\t",  res["Time"], "\t" ,res["Children"], "\t", res["Adults"]
                    )
            else:
                print("No reservations found.")
    except FileNotFoundError:
        print("No reservations found.")


def clearReservation():
    print("Delete Reservation")
    print("------------------")
    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()
        
            if lines:
                print("Current Reservations:")
                print("No.\tName\tDate\tTime\tChildren\tAdults\t")
                print("="*70)
                
                reservations = []
                reservation = {}
                for line in lines:
                    line = line.strip()
                    if line:
                        key, value = line.split(": ")
                        reservation[key] = value
                    else:
                        reservations.append(reservation)
                        reservation = {}
            
                for idx, res in enumerate(reservations, start=1):
                    print(idx, "t\n", res["Name"], "\t", res["Date"], "\t",  res["Time"],res["Children"], "\t", res["Adults"])
            
                print("\nSelect the reservation number to delete (0 to cancel):")
                choice = int(input())
            
                if choice != 0 and 1 <= choice <= len(reservations):
                    with open("data.txt", "w") as file:
                        for idx, line in enumerate(lines):
                            if idx < (choice - 1) * 6 or idx >= choice * 6:
                                file.write(line)
                    print("Reservation deleted.")
                elif choice == 0:
                    print("Deletion canceled.")
                else:
                    print("Invalid selection.")
            else:
                print("No reservations found.")
    except FileNotFoundError:
        print("No reservations found.")
        
def calculate_subtotal_with_fee(reservation):
    adults = int(reservation["Adults"])
    children = int(reservation["Children"])
    subtotal = (adults * 500) + (children * 300)
    return subtotal

def calculate_subtotal(reservation):
   
    print("Reservations")
    print("No.\tName\tDate\t\tTime\tChildren\tAdults\tSubtotal")
    print("="*70)

    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()
            if lines:
                reservations = []
                reservation = {}
                for line in lines:
                    line = line.strip()
                    if line:
                        key, value = line.split(": ")
                        reservation[key] = value
                    else:
                        reservations.append(reservation)
                        reservation = {}
                
                for idx, res in enumerate(reservations, start=1):
                    adults = int(res["Adults"])
                    children = int(res["Children"])
                    subtotal = (adults * 500) + (children * 300)
                    total_adults = 0
                    total_children = 0
                    grand_total = 0
                    print(
                        idx,"\t", res["Name"], "\t", res["Date"], "\t",  res["Time"], "\t", res["Children"], "\t", res["Adults"], "\t", subtotal
                    )
                    total_adults += int(res["Adults"])
                    total_children += int(res["Children"])
                    grand_total += calculate_subtotal_with_fee(res)
                print("Total Adults:", total_adults, "\nTotal Children: ", total_children, "\nGrand Total:", grand_total)

            else:
                print("No reservations found.")
    except FileNotFoundError:
        print("No reservations found.")
        

        
choice = input("Enter your choice: ")
while choice != '5':
    if choice == "1":
        name = input("Enter your name: ")
        date = input("Enter the reservation date (YYYY-MM-DD): ")
        time = input("Enter the reservation time (HH:MM AM/PM): ")
        child = int(input("Enter the number of children: "))
        adult = int(input("Enter the number of adults: "))
        res = reservation.Reservation(name, date, time, adult, child)
        res.getReservation()
        choice = input("Enter your choice: ")
    elif choice == "2":
        viewReservation()
        choice = input("Enter your choice: ")
    elif choice == "3":
        clearReservation()
        choice = input("Enter your choice: ")
    elif choice == "4":
        calculate_subtotal(reservation=reservation)
        choice = input("Enter your choice: ")
    else:
        print("invalid input")
        choice = input('Enter your choice: ')
else:
    print("Thank you!")