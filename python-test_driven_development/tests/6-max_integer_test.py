#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class max_integer_test(unittest.TestCase):
    """ """
    def test_ordered_list(self):
        """ test ordered list of integers """
        self.assertEqual(max_integer(ordered = [1, 2, 4, 6]), 6)

    def test_unordered_list(self):
        """ test unordered list of integers """
        self.assertEqual(max_integer(unordered = [3, 1, 7, 2]), 7)
    
    def test_empty_list(self):
        """ test empty list """
        self.assertEqual(max_integer(empty = []), None)
    
    def test_one_element(self):
        """ test list with only one element """
        self.assertEqual(max_integer(one_element = [3]), 3)
    
    def test_string(self):
        """ test string as input """
        self.assertEqual(max_integer(streeng = ["Hello"]))