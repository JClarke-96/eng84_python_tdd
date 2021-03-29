# Let's create tests to check if code would run without errors

from simple_calc import SimpleCalc  # Import file and class where code will be
import unittest     # Import unittest to inherit TestCase


class CalcTest(unittest.TestCase):
    calc = SimpleCalc()

    def test_add(self): # Naming convention - using 'test' in name of function
        self.assertEqual(self.calc.add(2, 4), 6)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4, 2), 2)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5, 3), 15)

    def test_divide(self):
        self.assertEqual(self.calc.divide(18, 6), 3)
