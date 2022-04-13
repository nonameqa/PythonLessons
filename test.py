from array import *

arr = array('i',[])

Num = int(input("Enter the length of array "))

for i in range(Num):
    values = int(input("Enter values in array "))
    arr.append(values)

print(arr)


search = int(input("Enter the value to check if it's in the array "))

s = 0
for k in arr:


    if k==search:
        print("Found the element " + str(search), "at index " + str(s))
        break
    s = s+1

else:
    print("Not in the array")



