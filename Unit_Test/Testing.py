import unittest

from math_function import is_even, modulo_func


class TestMathFunction(unittest.TestCase):
    def test_modulo_func_zero(self):
        num = 2
        result = modulo_func(num)
        return self.assertEqual(0, result, "Function bad boy")

    def test_modulo_func_zero_boundary1(self):
        num = -2
        result = modulo_func(num)
        return self.assertEqual(0, result, "Function bad boy")

    def test_is_even_true_boundary1(self):
        num = 4
        result = is_even(num)
        return self.assertTrue(result)

    def test_is_even_true_boundary2(self):
        num = 0
        result = is_even(num)
        return self.assertTrue(result)

    def test_is_even_true_boundary3(self):
        num = -2
        result = is_even(num)
        return self.assertTrue(result)
