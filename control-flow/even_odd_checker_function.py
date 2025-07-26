def even_or_odd_number():
    number_to_check=int(input("Enter an integer number >:"))
    if number_to_check%2==0:
        print(f"The number :{number_to_check} is an even number ")
    elif number_to_check% 2!=0:
        print(f"The number : {number_to_check} is an odd number.")
    else:
        print("Not defined! try to use an integer number") 
even_or_odd_number()           
        