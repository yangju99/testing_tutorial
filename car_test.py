import unittest
import random

from car import Car

# The setUp() method creates a new Car object before each test method, 
# ensuring that each test is independent and unaffected by the state of previous tests.
class TestCar(unittest.TestCase):
   def setUp(self):
       self.car = Car()

# test code for car.__init__ 
# The default values of all attributes must be 0
class TestInit(TestCar):
   def test_initial_speed(self):
       self.assertEqual(self.car.speed, 0) # assertEqual(a, b) is for checking if the values of a and b are equal


   def test_initial_odometer(self):
       self.assertEqual(self.car.odometer, 0)

   def test_initial_time(self):
       self.assertEqual(self.car.time, 0)

# test code for car.change_speed method
class TestChangeSpeed(TestCar):
   def test_change_speed(self):
       self.car.change_speed(7)
       self.assertEqual(self.car.speed, 7) # expected output = 0 + 7 = 7 

   def test_multiple_speed_change(self):
       total_change = 0
       for _ in range(3):
           change = random.randint(0, 10)
           total_change += change
           self.car.change_speed(change)
       self.assertEqual(self.car.speed, total_change)

# test code for car.get_current_speed method
class TestGetCurrentSpeed(TestCar):
   def test_get_current_speed_from_start(self):
       self.assertEqual(self.car.get_current_speed(), 0) 

   def test_get_current_speed_after_change(self):
       self.car.change_speed(27)
       self.assertEqual(self.car.get_current_speed(), 27)