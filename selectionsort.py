def sort(list):

    for i in range(4):
        minpos = i
        for j in range(i,5):
            if list[j] < list[minpos]:
                minpos = j


        temp = list[i]
        list[i] = list[minpos]
        list[minpos] = temp







list = [20,70,34,93,24]

sort(list)

print(list)