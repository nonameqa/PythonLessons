from numpy import *

def matrix():
    m1 = array([
        [1,2,3],
        [4,5,6],
        [6,9,1]
    ])

    m2 = array([
        [1,2],
        [4,5],
        [6,9]
    ])

    result = array([
                   [0,0],
                   [0,0],
                   [0,0]
    ])


    for i in range(len(m1)):
        for j in range(len(m2[0])):
            for k in range(len(m2)):

                result[i][j] += m1[i][k] * m2[k][j]

    print(result)

matrix()
