number1=int(input("Enter the first number :"))
number2=int(input("Enter the seconf number for division: "))

try: 
    quotient=number1/number2
except  ZeroDivisionError:
    print("Can not perform division by zer0")  
else:
    print("The quotient is equal to :",quotient)      
