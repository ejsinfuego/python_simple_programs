import numpy as np

arr = []

def getthenumber():
    enter = int(input("Please enter numbers: "))
    inc = arr.append(enter)
    while True:
        flag = len(arr)
        if flag != 5:
            new = int(input("Please enter a numbers: "))
            inc = arr.append(new)
            print(arr)
        else:
            print("The number you have provided were: ")
            for i in arr:
                print("-" + " " + "%s" % i)
            return
        
def check(arr, l, r, target):
    
    # Check base case
    while l <= r:

        mid = int(l + (r - l) // 2)
        #print(mid)
                
        if arr[mid] == target:
            return mid
           
        elif target < arr[mid]:
            return check(arr, l, mid-1, target)
        
        else:
            return check(arr, mid+1, r, target)
    return -1

getthenumber()
target = int(input("Please input the number you want to search: "))
result = check(arr, 0, len(arr)-1, target) + 1


if result != -1:
    print("The element is on index %s" % result)
else:
    print("Element is not present in the array")