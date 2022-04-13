from threading import *
from time import sleep

"""
class Hello(Thread):

    def run(self):
        for i in range(10):
            print("Hello")
            sleep(1)

class Hi(Thread):

    def run(self):
        for i in range(10):
            print("Hi")
            sleep(1)


t1 = Hello()
sleep(0.2)
t2 = Hi()

t1.start()
sleep(0.2)
t2.start()

t1.join()
t2.join()
print("Bye")
"""

f = open('Mydata','r')

f1 = open('abc', 'w')

f1.write("Something in the way")

f2 = open('abc','a')
f2.write("Nirvana")

for data in f:
   f2.write(data)