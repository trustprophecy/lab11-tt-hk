# [https://github.com/trustprophecy/lab11-tt-hk](https://github.com/trustprophecy/lab11-tt-hk)
# Partner 1: Trust Thomas

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-4, 7), 3)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(4, 10), -6)
        self.assertEqual(subtract(-5, -5), 0)

    def test_multiply(self):  # 3 assertions
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(-2, 5), -10)
        self.assertEqual(mul(0, 9), 0)

    def test_divide(self):  # 3 assertions
        self.assertAlmostEqual(div(2, 10), 5.0)
        self.assertAlmostEqual(div(-2, 10), -5.0)
        self.assertAlmostEqual(div(4, 1), 0.25)

    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2.0)
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(math.e, math.e), 1.0)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1, 10)

    ######## Partner 1
    def test_log_invalid_argument(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(10, 0)

    def test_hypotenuse(self):  # 3 assertions
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(-3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self):  # 3 assertions
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(0), 0.0)

if __name__ == "__main__":
    unittest.main()
