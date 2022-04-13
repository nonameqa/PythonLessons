from math import factorial


class A:

    def __init__(self,a,b):
        self.a = a
        self.b = b


    def Sum(self):
        self.c = (self.a + self.b)
        print(self.c)



class B(A):

    def __init__(self,a,b):
        self.a = a
        self.b = b


    def sub(self):
        self.c = (self.a - self.b)
        print(self.c)




class C(B):

    def __init__(self,a,b):
        self.a = a
        self.b = b



    def mult(self):
        self.c = (self.a * self.b)
        print(self.c)


class D:

    def __init__(self,num):
        self.num = num

    @staticmethod
    def facto(num):

            if num == 1:
                return 1
            else:
                return num * facto(num-1)


b1 = B(10,5)
b1.sub()
b1.Sum()

c1 = C(20,10)
c1.mult()
c1.sub()
c1.Sum()

d1 = D(5)
print(d1.facto(5))

