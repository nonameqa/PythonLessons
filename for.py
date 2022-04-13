from numpy import *

arr = array([1,2,3,4,5])

k = 0
for i in (arr):
    if k<= len(arr):
        arr[k] = arr[k] + 5
        k = k + 1

print(arr)


arr1 = array([10,15,20,25,30])

l=0
while(l < len(arr1)):
    arr1[l] +=5
    l +=1


print(arr1)