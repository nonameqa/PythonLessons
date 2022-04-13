def ifprime(Num):
    for i in range(2,Num):
        if Num ==1:
            print("1")
            break
        elif Num%i==0:
            print("Not a prime number")
            break
        else:
            print("Prime Number")
            break
    return Num


UserInput = int(input("Enter a number to check "))

Result = ifprime(UserInput)

print(Result)

