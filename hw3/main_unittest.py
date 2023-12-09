from main import even_odd_number, number_in_interval
import unittest

# python -m unittest main_unittest.py -v
#coverage run -m unittest main_unittest.py
# coverage report

class Test(unittest.TestCase):
    
    def test_even_odd_number_test(self):
        self.assertTrue(even_odd_number(8))

    def test_even_not_odd_number_test(self):
        self.assertFalse(even_odd_number(3))

    def test_number_in_interval(self):
        self.assertTrue(number_in_interval(50))

    def test_number_in_interval_bottom_limit(self):
        self.assertFalse(number_in_interval(25))

    def test_number_in_interval_top_limit(self):
        self.assertFalse(number_in_interval(100))