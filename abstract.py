from abc import ABC, abstractmethod

class Computer(ABC):
    abstractmethod
    def process(self):
        pass


class Laptop(Computer):
    def process(self):
        print("It's running")

class Programmer():
    def work(self,com):
        print("Fixing bugs")
        com.process()
#com1 = Computer()

lap1 = Laptop()
lap1.process()

prog1 = Programmer()
prog1.work(lap1)