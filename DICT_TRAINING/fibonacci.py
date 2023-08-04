currentNumber = 0
number2 = input('Enter a number to determine the fibonacci sequence: ')
result= 1
for i in range(int(number2)):
    print(result)
    result = result + currentNumber
    currentNumber = result - currentNumber