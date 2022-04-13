class Student():

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1,m2)
        return s3

    def __gt__(self, other):
        r1 = self.m1 + other.m1
        r2 = self.m2 + other.m2
        if r1 > r2:
            return True
        else:
            return False




s1 = Student(10, 20)
s2 = Student(30, 40)

s3 = s1 + s2

print(s3.m2)


if s1 > s2:
    print("S1 wins")

else:
    print("S2 wins")