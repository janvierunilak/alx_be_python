import random

# Generate a list of 20 random numbers between 1 and 10 (with possible duplicates)
random_numbers = [random.randint(1, 10) for _ in range(20)]

print("Original list with possible duplicates:")
print(random_numbers)

# Use set to remove duplicates
unique_numbers = set(random_numbers)

print("\nUnique numbers (duplicates removed):")
print(unique_numbers)
