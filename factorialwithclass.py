


class D:

    #def __init__(self,num):
     #   self.num = num


    def facto(self,num):

            if num == 0:
                return 1
            else:
                num = num * self.facto(self,num - 1)
            return num



d1 = D()

print(d1.facto(5))