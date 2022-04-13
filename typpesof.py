from array import *


# List  (values can be changed)_

list = [6.6,0,"dhj","hd",-5]

# Tuple  (values can't be changed)

tuplee = (1,8,36,34)

print(tuplee[2])     # to fetch []


#set  (collection of unique elements) (cannot be sure of order of sequence so cannot change using index)

s = {3,4,5,5}

print(s)

s.remove(5)

print(s)


#dictionary  (key value pair)

data = {1:'tarun',2:'Tokas'}

print(data)

print(data[2])    #(to fetch value)

print(data.get(2))

keys = ['tokas','tarun']
values = ['First','last']

dicti = dict(zip(keys,values))

print(dicti)

# Array

arr1 = array('i',[1,2,3,4,5,])   # without numpy - from array import *

print(arr1)

newarr = array(arr1.typecode, (a for a in arr1))

print(newarr)
#with numpy

arr2 = array([1,2,4])

