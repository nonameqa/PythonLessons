class A:

    def factorial(num):

        if num == 0:
            return 1
        else:

            return num * (factorial(num - 1))


V = int(input("Enter the value"))

print(factorial(V))

""" f = 1
 for i in range(1,num+1):
     f = f*i
 return f

"""
# a=1