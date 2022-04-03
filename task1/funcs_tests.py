import unittest
import funcs

# class for test cases
class TestCases(unittest.TestCase):

   #test case #1 for function f(x)
   def test_f_1(self):
      y=funcs.f(3)
      print("test_f_1 for f(x): ", y)

   #test case #2 for function f(x)
   def test_f_2(self):
      y=funcs.f(5)
      print("test_f_2 for f(x): ", y)

   #test case #3 for function g(x,y)
   def test_f_3(self):
      y=funcs.g(1,2)
      print("test_f_3 for g(x,y): ", y)

   #test case #4 for function g(x,y)
   def test_f_4(self):
      y=funcs.g(3,4)
      print("test_f_4 for g(x,y): ", y)

   #test case #5 for function hypotenuse(a,b)
   def test_f_5(self):
      y=funcs.hypotenuse(3,4)
      print("test_f_5 for hypotenuse(a,b): ", y)

   # test case #6 for function hypotenuse(a,b)
   def test_f_6(self):
      y = funcs.hypotenuse(1, 1)
      print("test_f_6 for hypotenuse(a,b): ", y)

   # test case #7 for function is_positive(a)
   def test_f_7(self):
      y = funcs.is_positive(2)
      print("test_f_7 for is_positive(a): ", y)

   # test case #8 for function is_positive(a)
   def test_f_8(self):
      y = funcs.is_positive(-1)
      print("test_f_8 for is_positive(a): ", y)

   # Run the unit tests.
if __name__ == '__main__':
   unittest.main()
