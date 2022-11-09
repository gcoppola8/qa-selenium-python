import unittest
import calculator


class CalculatorTestCase(unittest.TestCase):

    def test_multiply(self):
        self.assertEqual(0, calculator.multiply(0, 110))
        self.assertEqual(0, calculator.multiply(0, 1))
        self.assertEqual(0, calculator.multiply(0, 0))
        self.assertEqual(0, calculator.multiply(0, -123))

        self.assertEqual(1, calculator.multiply(1, 1))
        self.assertEqual(12, calculator.multiply(1, 12))
        self.assertEqual(123, calculator.multiply(1, 123))
        self.assertEqual(-4, calculator.multiply(1, -4))

        self.assertEqual(60, calculator.multiply(12, 5))
        self.assertEqual(-4, calculator.multiply(2, -2))

    def test_add(self):
        self.assertEqual(1, calculator.add(0, 1))
        self.assertEqual(12, calculator.add(0, 12))
        self.assertEqual(123, calculator.add(0, 123))

        self.assertEqual(123, calculator.add(101, 22))

    def test_subtract(self):
        self.assertEqual(0, calculator.subtract(2, 2))
        self.assertEqual(-10, calculator.subtract(0, 10))
        self.assertEqual(99, calculator.subtract(100, 1))

    def test_divide(self):
        self.assertEqual(1.0, calculator.divide(10, 10))
        self.assertEqual(1.0, calculator.divide(5, 5))
        self.assertEqual(12, calculator.divide(120, 10))


if __name__ == "__main__":
    unittest.main()
