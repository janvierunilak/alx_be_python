secret_number=7
guess_count=0
guess=0

while  guess!=secret_number:
    guess_count+=1
    guess=int(input(f"Enter a number to guess (between 1 --10) >: "))
print(f"congratulations, You guessed it in {guess_count} tries!")

