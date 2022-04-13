from numpy import *

#adding 5 to each element

arr = array([1,2,3,4,5])

"""
for i in arr:
    k = i+5
    arr[i-1] = k


print(arr)

i = 0
while(i<len(arr)):
    k = i+6
    arr[i] = k
    i = i+1

print(arr)
"""

arr1 = array([1,2,3,4,5])

arr1 = arr1 +5

print(arr1)


#adding two array
arr2 = arr1 + arr

print(arr2)

#sum of elements
print(sum(arr2))

#concatenate two array
print(concatenate([arr1,arr]))

#copying array
arr2=arr1

'''
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))

'''
# copy array but diffrenet address (shallow) value changes both
'''
arr2 = arr1.view()

arr1[1] = 91
print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))
'''

# copy but deep value. Only arr2 will change

arr2 = arr1.copy()

arr1[1] = 31

print(arr1)
print(arr2)

print(id(arr1))
print(id(arr2))


# sum of elements
arr10 = array([1,5,10,15])
sum = 0

for i in arr10:
    sum = sum + i



print(sum)

