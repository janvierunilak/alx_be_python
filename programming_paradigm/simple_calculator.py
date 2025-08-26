# simple_calculator.py

class SimpleCalculator:
    """A simple calculator class to perform basic arithmetic operations."""

    def add(self, a, b):
        """Returns the sum of two numbers."""
        return a + b

    def subtract(self, a, b):
        """Returns the difference of two numbers."""
        return a - b

    def multiply(self, a, b):
        """Returns the product of two numbers."""
        return a * b

    def divide(self, a, b):
        """
        Returns the quotient of two numbers.
        Handles division by zero by returning None.
        """
        if b == 0:
            return None
        f"Division by zero is not feasible "
        return a / b
