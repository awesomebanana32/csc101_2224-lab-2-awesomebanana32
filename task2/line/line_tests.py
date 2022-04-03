import unittest
import line


# this is the LineTest class
class LineTests(unittest.TestCase):

    # this the test_line function to test the Line class
    def test_line(self):
        # The following line should show a warning on the value "shoe".
        result = line.Line("shoe", 2, 3, 4)
        print(result)
        self.assertEqual(result.x1, 1)
        self.assertEqual(result.y1, 2)
        self.assertEqual(result.x2, 3)
        self.assertEqual(result.y2, 4)

    # this is the test_line_again function to test the Line class a second time
    def test_line_again(self):
        result = line.Line(5,6,7,8)
        self.assertEqual(result.x1, 5)
        self.assertEqual(result.y1, 6)
        self.assertEqual(result.x2, 7)
        self.assertEqual(result.y2, 8)
        print(result)

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()

