import unittest
from calculator import add, sub, mul, div, pow_func


class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(10, 5), 15.0)
        self.assertEqual(add(-3, -5), -8.0)

    def test_sub(self):
        self.assertEqual(sub(10, 5), 5.0)

    def test_mul(self):
        self.assertEqual(mul(10, 5), 50.0)

    def test_div(self):
        self.assertEqual(div(10, 2), 5.0)
        self.assertEqual(div(10, 0), "Лучше не надо делить на 0")

    def test_pow(self):
        self.assertEqual(pow_func(2, 3), 8.0)


if __name__ == "__main__":
    unittest.main()
