
class Time:
     pass
 
def addTime(t1, t2):
     sum = Time()
     sum.hours = t1.hours + t2.hours
     sum.minutes = t1.minutes + t2.minutes
     sum.seconds = t1.seconds + t2.seconds
     return sum

def printTime(time):
     print (str(time.hours) + ":" + \
             str(time.minutes) + ":" + \
             str(time.seconds))
        
currentTime = Time()
currentTime.hours = 5
currentTime.minutes = 12
currentTime.seconds = 23

breadTime = Time()
breadTime.hours = 6
breadTime.minutes = 11
breadTime.seconds = 2

doneTime = addTime(currentTime, breadTime)
printTime(doneTime)