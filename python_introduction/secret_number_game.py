import random

print("🎯 Welcome to the Secret Number Guessing Game!")

while True:
    secret_number = random.randint(1, 10)
    guess_count = 0
    guessed_correctly = False

    while not guessed_correctly:
        try:
            guess = int(input("\nGuess the secret number (between 1 and 10): "))
            guess_count += 1

            match guess:
                case n if n == secret_number:
                    print(f"🎉 Congratulations, you guessed it in {guess_count} {'try' if guess_count == 1 else 'tries'}!")
                    guessed_correctly = True
                case n if n > secret_number:
                    print("📈 Oops, your guess is a bit high. Try again!")
                case n if n < secret_number:
                    print("📉 Nope, your guess is a bit low. Give it another shot!")
        except ValueError:
            print("⚠️ Please enter a valid number!")

    # Ask if user wants to play again
    play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
    if play_again not in ["yes", "y"]:
        print("👋 Thanks for playing! Goodbye!")
        break
