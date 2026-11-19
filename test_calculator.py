# https://github.com/trustprophecy/lab11-tt-hk 
# Partner 1: Trust Thomas

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
# Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

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
