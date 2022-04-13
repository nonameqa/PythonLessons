class  A():

    def __init__(self,a,b):
        self.a = a
        self.b = b


    def sum(self, a = None, b = None, c = None):
        sum = 0

        if a!=None and b!=None and c!=None:

            sum = a+b+c

        elif a!=None and b!=None:

            sum = a+b

        else:

            sum = a

        return sum




a1 = A(10,20)
print(a1.sum(1,2,3))



class B():

    def show(self):
        print("Override this")

class C(B):

    def show(self):
        print("Overriding here")

b1 = B()
c1 = C()

print(c1.show())
print(b1.show())