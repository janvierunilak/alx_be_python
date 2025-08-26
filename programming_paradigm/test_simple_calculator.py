# test_simple_calculator.py

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """
        Set up a new SimpleCalculator instance before each test.
        This method is called automatically by the test runner.
        """
        self.calc = SimpleCalculator()

    # Test for the 'add' method
    # ---------------------------
    def test_addition(self):
        """Test the add method with integers, negatives, and floats."""
        self.assertEqual(self.calc.add(2, 3), 5, "Should be 5")
        self.assertEqual(self.calc.add(-1, 1), 0, "Should be 0")
        self.assertEqual(self.calc.add(-5, -5), -10, "Should be -10")
        self.assertEqual(self.calc.add(10, 0), 10, "Should be 10")
        self.assertAlmostEqual(self.calc.add(1.5, 2.5), 4.0, "Should be 4.0")

    # Test for the 'subtract' method
    # --------------------------------
    def test_subtraction(self):
        """Test the subtract method with various numeric inputs."""
        self.assertEqual(self.calc.subtract(10, 5), 5, "Should be 5")
        self.assertEqual(self.calc.subtract(-1, 1), -2, "Should be -2")
        self.assertEqual(self.calc.subtract(-1, -1), 0, "Should be 0")
        self.assertEqual(self.calc.subtract(5, 10), -5, "Should be -5")
        self.assertAlmostEqual(self.calc.subtract(
            5.5, 2.2), 3.3, "Should be 3.3")

    # Test for the 'multiply' method
    # --------------------------------
    def test_multiplication(self):
        """Test the multiply method, including multiplication by zero."""
        self.assertEqual(self.calc.multiply(3, 7), 21, "Should be 21")
        self.assertEqual(self.calc.multiply(-1, 5), -5, "Should be -5")
        self.assertEqual(self.calc.multiply(-2, -4), 8, "Should be 8")
        self.assertEqual(self.calc.multiply(10, 0), 0, "Should be 0")
        self.assertAlmostEqual(self.calc.multiply(
            1.5, 2.0), 3.0, "Should be 3.0")

    # Test for the 'divide' method
    # ------------------------------
    def test_division(self):
        """Test the divide method, including the division by zero edge case."""
        self.assertEqual(self.calc.divide(10, 2), 5, "Should be 5")
        self.assertEqual(self.calc.divide(-10, 2), -5, "Should be -5")
        self.assertAlmostEqual(self.calc.divide(5, 2), 2.5, "Should be 2.5")

        # Test for the division by zero edge case
        self.assertIsNone(self.calc.divide(10, 0),
                          "Division by zero should return None")
        self.assertIsNone(self.calc.divide(-5, 0),
                          "Division by zero should return None")
        self.assertIsNone(self.calc.divide(
            0, 0), "Division of zero by zero should return None")


if __name__ == '__main__':
    unittest.main()
