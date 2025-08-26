import sys 
from bank_account import BankAccount


def main():
    """
    Main function to handle command-line interactions with the BankAccount class.
    """
    account = BankAccount(100)  # Example starting balance for testing

    if len(sys.argv) < 2:
        print("Usage: python main-0.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    try:
        command_parts = sys.argv[1].split(':')
        command = command_parts[0]
        amount = float(command_parts[1]) if len(command_parts) > 1 else None
    except ValueError:
        print("Error: Amount must be a number.")
        sys.exit(1)
    except IndexError:
        # This handles cases where only the command is given, e.g., "display"
        command = sys.argv[1]
        amount = None

    if command == "deposit":
        if amount is not None:
            try:
                account.deposit(amount)
                print(f"Deposited: ${amount:.2f}")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Error: Deposit command requires an amount. Usage: deposit:<amount>")
    elif command == "withdraw":
        if amount is not None:
            try:
                if account.withdraw(amount):
                    print(f"Withdrew: ${amount:.2f}")
                else:
                    print("Insufficient funds.")
            except ValueError as e:
                print(f"Error: {e}")
        else:
            print("Error: Withdraw command requires an amount. Usage: withdraw:<amount>")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command. Commands: deposit, withdraw, display")

if __name__ == "__main__":
    main()