# Let's create tests to check if code would run without errors

from simple_calc import SimpleCalc  # Import file and class where code will be
import unittest     # Import unittest to inherit TestCase


class CalcTest(unittest.TestCase):
    calc = SimpleCalc()

    def test_add(self): # Naming convention - using 'test' in name of function
