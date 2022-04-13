def fib(n):


    a = 0
    b = 1

    if n <0:
        print("GTFO")
    else:
        print(a)
        print(b)
    for i in range(2,n):
        r = a + b
        a = b
        b = r

        print(r)

fib(2)



