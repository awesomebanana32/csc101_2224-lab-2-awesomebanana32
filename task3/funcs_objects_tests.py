import unittest
import objects
import funcs

class TestCases(unittest.TestCase):
   def test_point(self):
      # Add code here to verify that a point is initialized correctly.
      pointA = objects.Point(1, 1)
      pointB = objects.Point(2, 2)

      distance = funcs.euclidean(pointA, pointB)
      print("print the result of test_point function: ", distance)

   def test_point_again(self):
      # Add code here to verify that a point is initialized correctly.
      pointA = objects.Point(1, 3)
      pointB = objects.Point(4, 4)

      distance = funcs.euclidean(pointA, pointB)
      print("print the result of test_point_again function:", distance)

   def test_circle(self):
      # Add code here to verify that a point is initialized correctly.
      centerA = objects.Point(1, 1)
      centerB = objects.Point(2, 2)

      overlapTrue = funcs.circle_overlap(centerA, 1, centerB, 2)
      print("True if the circles overlap in test_circle func:", overlapTrue)

   def test_circle_again(self):
      # Add code here to verify that a point is initialized correctly.
      centerA = objects.Point(1, 1)
      centerB = objects.Point(10, 10)

      overlapTrue = funcs.circle_overlap(centerA, 1, centerB, 2)
      print("True if the circles overlap in test_circle_again func:", overlapTrue)

   # Add other testing functions for distance and circles_overlap.


# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

