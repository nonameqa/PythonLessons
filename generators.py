def topten():

    num = 1
    while num <=10:
        sq = num*num
        yield sq
        num+=1


values = topten()

for i in values:
    print(i)