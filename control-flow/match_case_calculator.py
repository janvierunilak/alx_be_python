num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
choose_the_operation=input("Choose the operation (+, -, *, / ): ")

match choose_the_operation :
    case "+":
        result=num1+num2
        print("The result is :", result)
    case "-":
        result=num1-num2
        print("The result is :", result)

    case "*":
        result=num1*num2
        print("The result is :", result)

    case "/":
        if num2==0:
            print("Can not divide by zero")
        else:
            result=num1/num2 
            print("The result is :", result)

    case _:
        print("Invalid!")
               