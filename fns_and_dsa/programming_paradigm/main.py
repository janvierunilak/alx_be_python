import sys
from bank_account import BankAccount


def main():
    account = BankAccount(100)

    if len(sys.argv) < 2:
        print("Usage : Python main-o.py <command>[:<amount>]")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command_parts = sys.argv[1].split(':')
    command = command_parts[0]

    amount = None
    if len(command_parts) > 1:
        try:
            amount = float(command_parts[1])
        except ValueError:
            print("Invalid amount. Please provide a numeric value. ")
        sys.exit(1)

    if command == "deposit" and amount is not None:
        if account.deposit(amount):
            print(f" The deposited amount is :${amount}")

    elif command == "withdraw" and amount is not None:
        if account.withdraw(amount):
            print(f"Withdrew: ${amount}")
        else:
            print("Insufficient funds or invalid amount. ")
    elif command == "display":
        print(account.display_balance)
    else:
        print("Invalid command")


if __name__ == "__main__":
    main()
