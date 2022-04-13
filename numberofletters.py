def numberofletters(lst):
    Namewithlengthofmorethan5 = 0

    for i in lst:

        if len(i)>=5:
            Namewithlengthofmorethan5+=1

    return Namewithlengthofmorethan5





lst = []

n = int(input("enter the number of users "))

for i in range(n):
    x=str(input("enter the name "))
    lst.append(x)

Namewithlengthofmorethan5 = numberofletters(lst)

print("Namewithlengthofmorethan5 is: {}".format(Namewithlengthofmorethan5))
