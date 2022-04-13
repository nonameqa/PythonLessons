from numpy import *
from array import *
"""
m1 = array('i',[
    [1,2,3],
    [4,5,6]])

m2 = array('i',[[2,4],
           [3,9],
           [6,8]])

result = array('i',[[],[]])

s=0
for i in m1:
    for j in m2:
        for k in m2:
            s += m1[i][k] * m2[k][j]


result[i][j] = sum

print(result)
"""
A = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

# take a 3x4 matrix
B = [[5, 8, 1, 2],
     [6, 7, 3, 0],
     [4, 5, 9, 1]]

result = [[0, 0, 0, 0],
          [0, 0, 0, 0],
          [0, 0, 0, 0]]


print(len(A))
print(len(B[0]))
# iterating by row of A
for i in range(len(A)):

    # iterating by column by B
    for j in range(len(B[0])):

        # iterating by rows of B
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

for r in result:
    print(r)
