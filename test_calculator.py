# [https://github.com/trustprophecy/lab11-tt-hk](https://github.com/trustprophecy/lab11-tt-hk)
# Partner 1: Trust Thomas

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
# Partner 1
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-2, 5), 3)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(4, 10), -6)

    def test_exponent(self):
        self.assertEqual(exp(2, 3), 8)
        self.assertEqual(exp(5, 0), 1)
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            div(10, 0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-1, 10)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)
if __name__ == "__main__":
    unittest.main()
