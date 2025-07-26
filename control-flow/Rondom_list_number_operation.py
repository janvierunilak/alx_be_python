import random
# Generate a list of 20 random numbers between 1 and 10 (with possible duplicates)

random_numbers_list= [random.randint(1,10) for _ in range (20)]
print(" Original list with possible duplicates : ")
print(" 20 random numbers on the list with duplicates :>",random_numbers_list)

unique_numbers_on_the_list= set(random_numbers_list)
print("\n Unique numbers (duplicates removed): ")
print(" Unique numbers on the list without duplicates are :> ",unique_numbers_on_the_list)
print("The Total unique numbers are >> ",len(unique_numbers_on_the_list))




