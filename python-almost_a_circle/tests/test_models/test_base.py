#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys

class TestBaseID(unittest.TestCase):
    def auto_id_test(self):
        b1 = Base()
        b2 = Base(78)
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 78)

    def test_id_type(self):
        base = Base(78)
        self.assertIsInstance(base.id, int)

    def test_to_json_string(self):
        data = [{'key': 'value'}]
        result = Base.to_json_string(data)
        self.assertEqual(result, '[{"key": "value"}]')

if __name__ == '__main__':
    unittest.main()
