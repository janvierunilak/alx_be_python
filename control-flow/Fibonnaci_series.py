def fibonacci_series(n):
    a, b=0,1
    while a < n:
        print(a, end=" ")
        a,b =b, a+b
    print()

fibonacci_series(500)        

