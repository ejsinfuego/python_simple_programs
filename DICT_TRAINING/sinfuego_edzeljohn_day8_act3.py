
class House:
    def __init__(self, floorSize, noOfFloors, noOfDoors):
        self.floorSize = floorSize
        self.noOfFloors = noOfFloors
        self.noOfDoors = noOfDoors

    def switchOn(self):
        print("Switch On")
        self.lightOpen()
        self.ovenOpen()

    def lightOpen(self):
        print("Light Open")

    def ovenOpen(self):
        print("Oven Open")
        
class TownHouse(House):
    def __init__(self, floorSize, noOfFloors, noOfDoors):
        super().__init__(floorSize, noOfFloors, noOfDoors)
        self.noOfFloors = 2
        self.noOfDoors = 3

    def display(self):
        print("Floor Size:", self.floorSize)
        print("Number of Floors:", self.noOfFloors)
        print("Number of Doors:", self.noOfDoors)

house = TownHouse(100, 2, 3)
house.display()
house.switchOn()
house.lightOpen()
