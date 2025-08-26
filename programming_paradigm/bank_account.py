
class BankAccount:
    """
    A simple bank account class to demonstrate OOP concepts.
    Encapsulates account balance and provides methods for deposit, withdrawal, and balance display.
    """

    def __init__(self, initial_balance=0):
        """
        Initializes a new BankAccount instance.

        Args:
            initial_balance (float, optional): The initial balance of the account. Defaults to 0.
        """
        if not isinstance(initial_balance, (int, float)) or initial_balance < 0:
            raise ValueError("Initial balance must be a non-negative number.")
        self.__account_balance = initial_balance  # Encapsulation: Use double underscore for "private" attribute

    def deposit(self, amount):
        """
        Deposits the specified amount into the account.

        Args:
            amount (float): The amount to deposit. Must be a positive number.
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Deposit amount must be a positive number.")
        self.__account_balance += amount

    def withdraw(self, amount):
        """
        Withdraws the specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw. Must be a positive number.

        Returns:
            bool: True if the withdrawal was successful, False otherwise (insufficient funds).
        """
        if not isinstance(amount, (int, float)) or amount <= 0:
            raise ValueError("Withdrawal amount must be a positive number.")
        if self.__account_balance >= amount:
            self.__account_balance -= amount
            return True
        else:
            return False

    def display_balance(self):
        """
        Prints the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.__account_balance:.2f}")