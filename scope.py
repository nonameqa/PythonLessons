a = 10  # global


def xyz():
    global a
    a = 12  # local

    print(a)



xyz()
print(a)


j = 10  # global


def xyz():

    j = 12  # local

    x = globals()['j']
    print(j)
    globals()['j'] = 71


xyz()
print(j)