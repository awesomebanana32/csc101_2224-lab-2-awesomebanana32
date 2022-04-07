# this is the Line class
class Line:

    # this implements the __init__ function
    def __init__(self,x1:float,y1:float,x2:float,y2:float):

        self.x1 = x1
        self.x2 = x2
        self.y1 = y1
        self.y2 = y2

    # this implements the __str__ function
    def __str__(self) -> str:
        return f"{self.x1},{self.y1},{self.x2},{self.y2}"
