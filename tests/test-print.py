#!/usr/bin/python3
import unittest
from io import StringIO
import sys
from print import say_my_name

class TestSayMyName(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = sys.__stdout__

    def test_normal_names(self):
        say_my_name("John", "Smith")
        self.assertEqual(self.held_output.getvalue(), "My name is John Smith\n")

    def test_first_name_only(self):
        say_my_name("John")
        self.assertEqual(self.held_output.getvalue(), "My name is John \n")

    def test_invalid_types(self):
        with self.assertRaises(TypeError):
            say_my_name(123, "Smith")
        with self.assertRaises(TypeError):
            say_my_name("John", 123)
        with self.assertRaises(TypeError):
            say_my_name(None)

if __name__ == '__main__':
    unittest.main()
