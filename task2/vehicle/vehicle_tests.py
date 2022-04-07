import unittest
import vehicle

# this is the vehicle test class
class VehicleTests(unittest.TestCase):

   # this is the first vehicle test
   def test_vehicle(self):

      result = vehicle.Vehicle(int(4), float(10), int(4), bool(True))
      print(result)
      self.assertEqual(result.wheels, int(4))
      self.assertEqual(result.fuel, float(10))
      self.assertEqual(result.doors, int(4))
      self.assertEqual(result.roof, bool(True))

   # we are going to test the vehicle class again
   def test_vehicle_again(self):
      result = vehicle.Vehicle(int(5), float(6), int(7), bool(True))
      print(result)
      self.assertEqual(result.wheels, int(5))
      self.assertEqual(result.fuel, float(6))
      self.assertEqual(result.doors, int(7))
      self.assertEqual(result.roof, bool(False))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

