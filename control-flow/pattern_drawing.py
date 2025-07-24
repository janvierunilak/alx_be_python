size=int(input("enter the size of your drawing pattern :"))

if size<=0:
    print("Enter a positive integer number .")
else:
    row=0    

while row <size:
    for col in range(size):
        print("* ",end=" ")
    print( )
    row+=1
            