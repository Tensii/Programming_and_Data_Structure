#!/usr/bin/python3
import unittest
from add import add_integer

class TestAddInteger(unittest.TestCase):
    def test_normal_integers(self):
        self.assertEqual(add_integer(1, 2), 3)
        self.assertEqual(add_integer(100, -2), 98)
        self.assertEqual(add_integer(2), 100)  # test default b=98

    def test_floats(self):
        self.assertEqual(add_integer(100.3, -2), 98)
        self.assertEqual(add_integer(100.3, 2.7), 102)

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            add_integer("Hello", 3)
        with self.assertRaises(TypeError):
            add_integer(2, "World")
        with self.assertRaises(TypeError):
            add_integer(None)

if __name__ == '__main__':
    unittest.main()
