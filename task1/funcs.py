# function f(x)
import math


def f(x):

  return (7*(x**2)+2*x)

# function g(x,y)
def g(x,y):

  return ((x**2)+(y**2))

#function hypotenuse
def hypotenuse(a,b):

  return (math.sqrt(a**2+b**2))

#function is_positive
def is_positive(a):

  if a > 0 :
    return True
  elif a <= 0 :
    return False

#func for calculating the Euclidean distance
def euclidean(a,b):

  return math.sqrt( ((b.x-a.x)**2)+((b.y-a.y)**2) )
