print("Congratulations !")
out_counter=5

while out_counter>0:
    inner_counter=1
    while inner_counter <=out_counter:
        print(inner_counter,end=" ")
        inner_counter+=1
    print()
    out_counter-=1
 
    # Multiplication table
print("well completed ")
print("Multiplication tables now !!!")

for i in range (1,11):
    for j in range(1,11):
        product=(i*j)
        print( f" {i} * {j} = {product} ",end=" \t ") 
    print()               

