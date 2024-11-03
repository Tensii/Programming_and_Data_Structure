#!/usr/bin/python3
import unittest
from divide import matrix_divided

class TestMatrixDivided(unittest.TestCase):
    def test_normal_division(self):
        matrix = [[1, 2, 3], [4, 5, 6]]
        result = matrix_divided(matrix, 2)
        self.assertEqual(result, [[0.5, 1.0, 1.5], [2.0, 2.5, 3.0]])

    def test_float_numbers(self):
        matrix = [[1.1, 2.2, 3.3], [4.4, 5.5, 6.6]]
        result = matrix_divided(matrix, 2)
        self.assertEqual(result, [[0.55, 1.1, 1.65], [2.2, 2.75, 3.3]])

    def test_zero_division(self):
        matrix = [[1, 2], [3, 4]]
        with self.assertRaises(ZeroDivisionError):
            matrix_divided(matrix, 0)

    def test_invalid_matrix(self):
        with self.assertRaises(TypeError):
            matrix_divided([[1, 2], [3, "4"]], 2)
        with self.assertRaises(TypeError):
            matrix_divided([[1, 2], [3]], 2)
        with self.assertRaises(TypeError):
            matrix_divided("not a matrix", 2)
        with self.assertRaises(TypeError):
            matrix_divided([[1, 2], [3, 4]], "2")

if __name__ == '__main__':
    unittest.main()
