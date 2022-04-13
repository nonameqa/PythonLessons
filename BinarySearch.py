pos = -1
def Binary(list,num):

    l = 0
    u = len(list)-1

    while l <=u:
        mid = (l+u)//2

        if list[mid] == num:
            globals()['pos'] = mid
            return True

        else:
            if list[mid]<num:
                l = mid+1
            else:
                u = mid-1

    return False

list = [10,20,50,60,294,483,540]

num = 202

if Binary(list,num):
    print("Found at", pos)

else:
    print("Not found")