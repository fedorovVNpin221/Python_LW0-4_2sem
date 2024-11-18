import unittest
from math import sqrt
from main import site, calculate


class TestCalculate(unittest.TestCase):

    def test_discriminant_greater_than_zero(self):
        with site.test_request_context():
            self.assertEqual(calculate(1, -3, 2), "Корни уравнения: x1 = 2.0, x2 = 1.0")

    def test_discriminant_equal_to_zero(self):
        with site.test_request_context():
            self.assertEqual(calculate(1, -4, 4), "Уравнение имеет единственный корень: x = 2.0")

    def test_discriminant_less_than_zero(self):
        with site.test_request_context():
            self.assertEqual(calculate(1, 2, 3), "Уравнение не имеет действительных корней")

if __name__ == '__main__':
    unittest.main()