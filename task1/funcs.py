# function f(x)
import math


def f(x:float) -> float:

  return (7*(x**2)+2*x)

# function g(x,y)
def g(x:float,y:float) -> float:

  return ((x**2)+(y**2))

#function hypotenuse
def hypotenuse(a:float,b:float) -> float:

  return (math.sqrt(a**2+b**2))

#function is_positive
def is_positive(a:float) -> bool:

   return a > 0

#func for calculating the Euclidean distance
def euclidean(a:float,b:float) -> float:

  return math.sqrt( ((b.x-a.x)**2)+((b.y-a.y)**2) )

