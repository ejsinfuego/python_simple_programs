class Time:
    pass

time = Time()
time.hours = 0
time.minutes = 0
time.seconds = 0

def increment(time, seconds):
    t = Time()
    time.seconds = time.seconds +seconds
    
    while time.hours >= 12:
        time.hours = time.hours - 12
    
    while time.seconds >= 60:
        time.seconds = time.seconds - 60
        time.minutes = time.minutes + 1
        
    while time.minutes >= 60:
        time.minutes = time.minutes - 60
        time.hours = time.hours + 1
    return t

def printTime(t):
    print(str(time.hours) + ":" + \
          str(time.minutes) + ":" + \
          str(time.seconds))
    
printTime(increment(time,30000))



        
 
          