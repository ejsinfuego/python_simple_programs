"""This is an example of list data structure created by Edzel John Sinfuego"""

def provide_number():
    number = list(input("Please provide any data type. " ))
    flag = len(number)
    while True:
        if flag < 5:
            print("Sorry but you lacked number of data you have provided.")
            del number[:]
            number = list(input("Please try again. " ))
            flag = len(number)
            if flag > 10:
                print(number)
                print("The data you have provided are:")
                flag = len(number)
                for i in number:
                    print("-" + " " + i)
                return
                
        else:
            print(number)
            print("The data you have provided are:")
            for i in number:
                print("-" + " " + i)
            return
    
provide_number()
exit()