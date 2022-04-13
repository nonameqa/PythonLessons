from functools import reduce
from numpy import  *

"""lst = [1,5,7,29,20]

Even = list(filter(lambda a : a%2==0, lst))

Odd = list(filter(lambda b: b%2!=0,lst))

print(Even)
print(Odd)

plus5 = list(map( lambda a: a+5,lst))

print(plus5)

sum = reduce(lambda a,b : a+b,lst)

print(sum)"""

arr1 = array([1,2,3,4,5])

Even1 = array(filter(lambda a: a%2==0,arr1))

sum1 = reduce(lambda a,b:a+b,arr1)

map2 = array(map(lambda a:a*3,arr1))

print(map2)