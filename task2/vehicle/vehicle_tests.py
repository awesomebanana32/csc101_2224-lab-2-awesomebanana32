import unittest
import vehicle

# this is the vehicle test class
class VehicleTests(unittest.TestCase):

   # this is the first vehicle test
   def test_vehicle(self):

      result = vehicle.Vehicle(4, 10, 4, 1)
      print(result)
      self.assertEqual(result.wheels, 4)
      self.assertEqual(result.fuel, 10)
      self.assertEqual(result.doors, 4)
      self.assertEqual(result.roof, 1)

   # we are going to test the vehicle class again
   def test_vehicle_again(self):
      result = vehicle.Vehicle(5, 6, 7, 8)
      print(result)
      self.assertEqual(result.wheels, 5)
      self.assertEqual(result.fuel, 6)
      self.assertEqual(result.doors, 7)
      self.assertEqual(result.roof, 8)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

