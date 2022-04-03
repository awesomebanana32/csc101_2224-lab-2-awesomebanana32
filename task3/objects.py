class Point:
    def __init__(self,x,y):

        self.x = x
        self.y = y

    def __str__(self):
        return f"{self.x},{self.y}"

class Circle:
    #need circle point and radius
    def __init__(self, cirle_point, radius):
        self.circle_point = circle_point
        self.radius = radius

    def __str__(self):
        return f"{self.circle_point},{self.radius}"