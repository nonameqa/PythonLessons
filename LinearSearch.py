pos = 0
def search(list,num):

    for i in list:
        if i == num:

            return True
        i = i + 1
        globals()['pos'] += 1
    return False






list = [2,4,3,5,4,7,8]

num = int(input("Enter a number"))
if search(list,num):
    print("Found at",pos)
else:
    print("Not found")