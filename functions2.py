
def type(lst):

    even = 0
    odd = 0

    for i in lst:
        if i%2==0:
            even+=1
        else:
            odd+=1

    return even,odd

lst = []

n = int(input("enter the length of the list"))

for i in range(n):
    x = int(input("enter the number into the list"))
    lst.append(x)

print(lst)

EVEN,ODD = type(lst)

print("Even are: {}".format(EVEN))
print("ODD are", ODD)