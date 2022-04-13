def sub(a,b):

    print(a-b)

def smartfunc(func):

    def inner(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return inner



sub = smartfunc(sub)

sub(3,7)