# this is the Vehicle class
class Vehicle:
    # implements the __init__ function
    def __init__(self,wheels,fuel,doors,roof):

        self.wheels = wheels
        self.fuel = fuel
        self.doors = doors
        self.roof = roof

    # implement the __str__ function
    def __str__(self):
        return f"{self.wheels},{self.fuel},{self.doors},{self.roof}"
