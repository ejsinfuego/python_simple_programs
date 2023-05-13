class Point:
    pass
    
blank = Point()

blank.x = 3.0
blank.y = 4.0

print(blank.y)
x = blank.x
print(x)

print('(' + str(blank.x) +  ' , ' + str(blank.y) + ')')
distanceSquared = blank.x * blank.x + blank.y * blank.y
print(distanceSquared)
print(blank)


p1 = Point()
p1.x = 3
p1.y = 4
p2 = Point()
p2.x = 3
p2.y = 4
print(p1 is p2)
p2 = p1
print(p1 is p2)

def samePoint(p1,p2):
    return (p1.x == p2.x) and (p1.y == p2.y)

p1 = Point()
p1.x = 3
p1.y = 4
p2 = Point()
p2.x = 3
p2.y = 4
samePoint(p1,p2)

def printPoint(p):
    print('('+str(p.x)+','+str(p.y)+')')   
printPoint(blank)

class Rectangle:
    pass

box = Rectangle()
box.width = 100.0
box.height = 200.0

box.corner = Point()
box.corner.x = 0.0
box.corner.y = 0.0

def findCenter(box):
    p = Point()
    p.x = box.corner.x + box.width/2.0
    p.y = box.corner.y - box.height/2.0
    return p

center = findCenter(box)
printPoint(center)

import copy
p1 = Point()
p1.x = 3
p1.y = 4
p2 = copy.copy(p1)
print(p1 == p2)
print(samePoint(p1,p2))

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        
    def __str__(self):
        return '(' + str(self.x) + ', '  + str(self.y) + ')'

