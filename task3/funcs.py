# function f(x)
import math


def f(x) -> float:

  return (7*(x**2)+2*x)

# function g(x,y)
def g(x,y) -> float:

  return ((x**2)+(y**2))

#function hypotenuse
def hypotenuse(a,b) -> float:

  return (math.sqrt(a**2+b**2))

#function is_positive
def is_positive(a) -> bool:

  if a > 0 :
    return True
  elif a <= 0 :
    return False

#func for calculating the Euclidean distance
def euclidean(a,b) -> float:

  return math.sqrt( ((b.x-a.x)**2)+((b.y-a.y)**2) )

def circle_overlap(circleA, radiusA, circleB, radiusB) -> bool:
  circle_distance = euclidean(circleA, circleB)
  #print("circle_distance", circle_distance)

  sum_of_the_radii = radiusA + radiusB
  #print("sum_of_the_radii", sum_of_the_radii)

  return (circle_distance < sum_of_the_radii)