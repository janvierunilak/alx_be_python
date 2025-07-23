value=input("Enter any value (number or string):")
match value:
    case int():
        print("You have intered a number:",value)
    case str():
        print("You have entered a String :",value)
    case _:
        print("You entered an invalid data type ! ")
