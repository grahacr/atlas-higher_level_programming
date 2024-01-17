#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """ """
    def test_ordered_list(self):
        """ test ordered list of integers """
        self.assertEqual(max_integer(test_list = [1, 2, 4, 6]), 6)

    def test_unordered_list(self):
        """ test unordered list of integers """
        self.assertEqual(max_integer([3, 1, 7, 2]), 7)

    def test_empty_list(self):
        """ test empty list """
        self.assertEqual(max_integer([]), None)

    def test_one_element(self):
        """ test list with only one element """
        self.assertEqual(max_integer([3]), 3)

    def test_negative_numbers(self):
        """ test list with negative numbers """
        self.assertEqual(max_integer([-5, -8, -9, -11]), -5)

    def test_mixed_numbers(self):
        """ test list of numbers with positive and negative values """
        self.assertEqual(max_integer([8, 4, -2, -4]), 8)
    
    def test_float_numbers(self):
        """ test list of floats """
        self.assertEqual(max_integer([4.3, 1.7, 9.8]), 9.8)
